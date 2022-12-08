import pandas as pd
from os.path import join

from Utils.constants import SNOMED_DIR, SNOMED_CSV
from Service.snomed_import import build_snomed_table_from_dict, snomed_record_count

def import_snomed_csv(app):
    with app.app_context():
        if snomed_record_count() == 0:
            snomed_dataset = pd.read_csv(join(SNOMED_DIR, SNOMED_CSV))
            build_snomed_table_from_dict(snomed_dataset.to_dict(orient='records'))