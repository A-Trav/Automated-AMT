from os import listdir, remove, makedirs
from os.path import isfile, join, exists
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