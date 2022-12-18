from os import listdir, remove, makedirs
from os.path import isfile, join, exists
from Schema.amt import amts_schema
from Schema.snomed import snomeds_schema
from Service.search import amt_query_all, snomed_query_all
import pandas as pd

from Utils.constants import DATA_DIR, SNOMED_CSV

def setup_data_dir():
    if not exists(DATA_DIR):
        makedirs(DATA_DIR)

def is_outdated_versions(current_version_date, latest_version_date):
    if (current_version_date != latest_version_date):
        return True
    return False

def delete_csv_dist_collection():
    [remove(join(DATA_DIR, file_name)) for file_name in listdir(DATA_DIR) if (isfile(join(DATA_DIR, file_name)) and not file_name == SNOMED_CSV)]

def retrieve_export_csv():
    amt_dist = pd.DataFrame(amts_schema.dump(amt_query_all())).drop(columns=['ID', 'snomed'])
    snomed_dist = pd.DataFrame(snomeds_schema.dump(snomed_query_all()))
    return amt_dist.merge(snomed_dist, how = 'left', on = 'MP_PT').to_csv(index = False)