import os, logging, json
import pandas as pd 

from Schema.amt import amts_schema
from Requests.get_distro_meta import get_distro_meta
from Requests.post_ncts_auth import get_auth_token
from Requests.get_distro_csv import get_distro_csv 
from Service.version import get_version, delete_versions, create_version 
from Utils.http import response_to_csv, xml_response_to_version
from Utils.lib import is_outdated_versions, delete_csv_dist_collection, setup_data_dir
from Utils.constants import DATA_DIR
from Service.amt_rebuild import delete_amt_table, rebuild_table_from_dict

from Model.version import Version

def importer_task(app):
    with app.app_context():
        print('Starting task')
        try:
            setup_data_dir()
            versions = xml_response_to_version(get_distro_meta())
            latest_version_key = sorted(versions.keys()).pop() 

            # get current version from database and see if latest version matches
            local_version = get_version()
            if (local_version is None or is_outdated_versions(local_version.date, str(latest_version_key))):
                # delete old files before downloading new one
                delete_csv_dist_collection()

                # download new dist
                token = get_auth_token().json()['access_token']
                csv_file_name = os.path.join(DATA_DIR, versions[latest_version_key]['file_name'])
                response_to_csv(get_distro_csv(versions[latest_version_key]['link'], token), csv_file_name)

                # load distribution into dataframe
                new_dataset = pd.read_csv(csv_file_name)

                # Replace ' ' with _ to match automatic column rename in sqlite db
                new_dataset.columns = new_dataset.columns.str.replace(' ', '_')
                # Duplicate the MP_PT column into a Snomed column for foreign key mapping
                new_dataset['Snomed'] = new_dataset.loc[:, 'MP_PT']

                # delete old dist and replace with new
                delete_amt_table()
                rebuild_table_from_dict(new_dataset.to_dict(orient='records'))

                delete_versions() 
                create_version(date = latest_version_key, 
                        file = versions[latest_version_key]['file_name'], 
                        link = versions[latest_version_key]['link'])
                
            else:
                logging.debug('Current AMT distribution is up to date.')
        except Exception as e:
            # This is where we will need to alert admin for via email of catastrophic failure 
            raise e

