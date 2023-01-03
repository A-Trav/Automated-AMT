"""
The create handler module: Create endpoint.

Provides the applications create REST methods for creating new database
records within the Snomed and Amt SQLite tables.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Schema.amt import amt_schema
from Schema.snomed import snomed_schema
from Service.create import create_amt, create_snomed
import logging

create = Blueprint('create', __name__)
"""The create endpoint blueprint"""

@create.post('/create/amt')
@jwt_required()
def post_amt_create():
    """
    The REST method used to create a new AMT record within the Flask applications SQLite database.
    This REST method requires JWT authetication.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        req = request.json['create']
        error = amt_schema.validate(req)
        
        if len(error) != 0:
            return jsonify(error), 401

        record = create_amt(req['CTPP_SCTID'], req['CTPP_PT'], req['ARTG_ID'], req['TPP_SCTID'],
            req['TPUU_PT'], req['TPP_PT'], req['TPUU_SCTID'], req['TPP_TP_SCTID'], req['TPP_TP_PT'],
            req['TPUU_TP_SCTID'], req['TPUU_TP_PT'], req['MPP_SCTID'], req['MPP_PT'], req['MPUU_SCTID'],
            req['MPUU_PT'], req['MP_SCTID'], req['MP_PT'])
        
        return amt_schema.jsonify(record)
    except:
        logging.exception('Create AMT handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400

@create.post('/create/snomed')
@jwt_required()
def post_snomed_create():
    """
    The REST method used to create a new SNOMED record within the Flask applications SQLite database. 
    This REST method requires JWT authetication.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        req = request.json['create']
        error = snomed_schema.validate(req)
        
        if len(error) != 0:
            return jsonify(error), 401

        record = create_snomed(req['MP_PT'], req['AU_Substance_SCTID'], req['Int_Substance_SCTID'])
        
        return snomed_schema.jsonify(record)
    except:
        logging.exception('Create SNOMED handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400