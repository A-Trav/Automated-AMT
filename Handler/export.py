from flask import Blueprint, Response, jsonify
from Utils.lib import retrieve_export_csv

import pandas as pd 

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
        return jsonify({'msg': 'The server could not process the request'}), 400  