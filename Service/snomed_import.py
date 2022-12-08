from Database.database import db
from Model.amt import Snomed

def snomed_record_count():
    return len(Snomed.query.all())

def build_snomed_table_from_dict(snomed_dict):
    db.session.bulk_insert_mappings(Snomed, snomed_dict)
    db.session.commit()