"""
The lib module: Random Utility functions.
"""

from os import listdir, remove, makedirs
from os.path import isfile, join, exists
from Schema.amt import amts_schema
from Schema.snomed import snomeds_schema
from Service.search import amt_query_all, snomed_query_all
import pandas as pd

from Utils.constants import DATA_DIR, SNOMED_CSV

def setup_data_dir():
    """
    Creates the applications Data directory, to store the AMT distribution CSV files.
    """
    if not exists(DATA_DIR):
        makedirs(DATA_DIR)

def is_outdated_versions(current_version_date, latest_version_date):
    """
    Checks if the current AMT distribution date matches the latest available AMT distribution date.

    :param current_version_date: The date of the applications current AMT distribution version
    :type current_version_date: Date
    :param latest_version_date: The date of the NCTS API latest AMT distribution version
    :type latest_version_date: Date
    :return: Boolean representation of whether the applications current version date is not the latest NCTS version
    :rtype: Boolean
    """
    if (current_version_date != latest_version_date):
        return True
    return False

def delete_csv_dist_collection():
    [remove(join(DATA_DIR, file_name)) for file_name in listdir(DATA_DIR) if (isfile(join(DATA_DIR, file_name)) and not file_name == SNOMED_CSV)]

def retrieve_export_csv():
    """
    Builds a pandas dataframe, which represents a merged and formatted implementation of the applications current
    Amt and Snomed SQLite tables.

    :return: The dataframe consisting of both the Amt and Snomed SQLite tables
    :rtype: Dataframe
    """
    amt_dist = pd.DataFrame(amts_schema.dump(amt_query_all())).drop(columns=['ID', 'snomed'])
    snomed_dist = pd.DataFrame(snomeds_schema.dump(snomed_query_all()))
    return amt_dist.merge(snomed_dist, how = 'left', on = 'MP_PT').to_csv(index = False)