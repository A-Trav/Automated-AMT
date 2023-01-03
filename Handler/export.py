"""
The export handler module: Export endpoint.

Provides the applications export REST method for exporting the applications
joined Amt and Snomed tables, as a CSV file.
"""

from flask import Blueprint, Response, jsonify
from Utils.lib import retrieve_export_csv
import logging 

export = Blueprint('export', __name__)

@export.get('/export')
def get_export():
    try:
        return Response(
            retrieve_export_csv(),
            mimetype="text/csv",
            headers={"Content-disposition":
            "attachment; filename=amt_snomed_export.csv"}
        )
    except:
        logging.exception('Export handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400  