"""
The snomed import service module: Snomed import services.

Provides the application with the modelled Snomed import functionality needed to 
construct the Snomed SQLite table.
"""

from Database.database import db
from Model.amt import Snomed
from Utils.app_logging import log

@log
def snomed_record_count():
    """
    Queries the Snomed SQLite database table to retrieve a record count.

    :return: The number of records found within the table
    :rtype: int
    """
    return len(Snomed.query.all())

@log
def build_snomed_table_from_dict(snomed_dict):
    """
    Populates the Snomed SQLite database table with values from the provided dict.

    :param snomed_dict: The dictionary containing the Snomed table records
    :type snomed_dict: dict
    """
    db.session.bulk_insert_mappings(Snomed, snomed_dict)
    db.session.commit()