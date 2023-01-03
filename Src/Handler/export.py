"""
The export handler module: Export endpoint.

Provides the applications export REST method for exporting the applications
joined Amt and Snomed tables, as a CSV file.
"""

from flask import Blueprint, Response, jsonify
from Utils.lib import retrieve_export_csv
import logging 

export = Blueprint('export', __name__)
"""The export endpoint blueprint"""

@export.get('/export')
def get_export():
    """
    The REST method used to export both the AMT and SNOMED distribution tables as a singularly joined and formatted table,
    that is then exported as a CSV file. This REST method requires JWT authentication.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
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