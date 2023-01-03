"""
The startup_tasks module: Application startup tasks.

Provides the application with tasks intended to be run on application startup.
"""

import pandas as pd
from os.path import join

from Utils.constants import SNOMED_DIR, SNOMED_CSV
from Service.snomed_import import build_snomed_table_from_dict, snomed_record_count

def import_snomed_csv(app):
    """
    Imports the applications SNOMED CSV file found within the Data directory, on in order for the
    application to populate it's Snomed table.

    :param app: The Flask application to provide context
    :type app: Flask Application
    """
    with app.app_context():
        if snomed_record_count() == 0:
            snomed_dataset = pd.read_csv(join(SNOMED_DIR, SNOMED_CSV))
            build_snomed_table_from_dict(snomed_dataset.to_dict(orient='records'))