"""
The amt rebuild service module: Amt table rebuild services.

Provides the application with the modelled functionality needed to support 
the import of a new AMT distribution into the Amt SQLite table.
"""

from Database.database import db
from Model.amt import Amt
from app_logging import log

@log
def delete_amt_table():
    Amt.query.delete()
    db.session.commit()

@log
def rebuild_table_from_dict(dist):
    db.session.bulk_insert_mappings(Amt, dist)
    db.session.commit()