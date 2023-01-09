"""
The amt rebuild service module: Amt table rebuild services.

Provides the application with the modelled functionality needed to support 
the import of a new AMT distribution into the Amt SQLite table.
"""

from Database.database import db
from Model.amt import Amt
from Utils.app_logging import log, min_log

@log
def delete_amt_table():
    """
    Deletes all records found within the AMT SQLite database table.
    """
    Amt.query.delete()
    db.session.commit()

@min_log
def rebuild_table_from_dict(dist):
    """
    Populates the Amt SQLite database table from a dictionary representation of an AMT distribution.

    :param dist: The new AMT distribution to import into the Amt SQLite database table
    :type dist: dict
    """
    db.session.bulk_insert_mappings(Amt, dist)
    db.session.commit()