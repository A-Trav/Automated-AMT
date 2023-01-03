"""
The snomed import service module: Snomed import services.

Provides the application with the modelled Snomed import functionality needed to 
construct the Snomed SQLite table.
"""

from Database.database import db
from Model.amt import Snomed
from app_logging import log

@log
def snomed_record_count():
    return len(Snomed.query.all())

@log
def build_snomed_table_from_dict(snomed_dict):
    db.session.bulk_insert_mappings(Snomed, snomed_dict)
    db.session.commit()