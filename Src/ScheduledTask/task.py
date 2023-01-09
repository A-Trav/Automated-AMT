"""
The task module: Application AMT import task.

Provides the applications AMT distribution import tasks to be run by the 
task scheduler on a daily basis.
"""

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
from SMTP.smtp import alert_admin_failure
from Auth.auth import reset_jwt
from Utils.app_logging import log

@log
def importer_task(app):
    """
    The task to be scheduler and run by the applications background scheduler. This task
    aims to check for updates for new AMT distributions provided by the NCTS API. If the task
    fails to run successfully, the registered admin user of the Flask application will be notified 
    via email.

    :param app: The current flask application to provide application context with
    :type app: Flask applicaton
    """
    with app.app_context():
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
                        
                # Invalidate admin jwt to prevent db operation conflict with new distribution
                reset_jwt(app)
                logging.info('AMT distribution importer task finished.')
            else:
                logging.info('Current AMT distribution is up to date.')
        except:
            logging.exception('AMT distribution update failure')
            alert_admin_failure()

