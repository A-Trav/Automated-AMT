"""
The update handler module: Update endpoint.

Provides the applications update REST methods for updating records in the
Snomed SQLite table. Updated records are queried based on
primary key or field filters.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Service.update import update_AU_Substance_SCTID_by_id, update_AU_Substance_SCTID_by_filters
from Service.update import update_Int_Substance_SCTID_by_id, update_Int_Substance_SCTID_by_filters
from Schema.snomed import snomed_schema
import logging

update = Blueprint('update', __name__)
"""The update endpoint blueprint"""

@update.put('/update/snomed/AU_Substance_SCTID/id')
@jwt_required()
def put_update_AU_Substance_SCTID_by_id():
    """
    The REST method used to update a SNOMED records AU_Substance_SCTID field from within the Flask 
    applications SQLite database, by ID.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        id = request.args['id']
        val = request.json['AU_Substance_SCTID']
        return snomed_schema.jsonify(update_AU_Substance_SCTID_by_id(id, val)) 
    except:
        logging.exception('Update SNOMED AU_Substance_SCTID by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/AU_Substance_SCTID')
@jwt_required()
def put_update_AU_Substance_SCTID_by_filters():
    """
    The REST method used to update a SNOMED records AU_Substance_SCTID field from within the Flask 
    applications SQLite database, by field filter/s.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        filters = request.json['filters']
        val = request.json['AU_Substance_SCTID']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400

        return snomed_schema.jsonify(update_AU_Substance_SCTID_by_filters(filters, val)) 
    except:
        logging.exception('Update SNOMED AU_Substance_SCTID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/Int_Substance_SCTID/id')
@jwt_required()
def put_update_Int_Substance_SCTID_by_id():
    """
    The REST method used to update a SNOMED records Int_Substance_SCTID field from within the Flask 
    applications SQLite database, by ID.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        id = request.args['id']
        val = request.json['Int_Substance_SCTID']
        return snomed_schema.jsonify(update_Int_Substance_SCTID_by_id(id, val)) 
    except:
        logging.exception('Update SNOMED Int_Substance_SCTID by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/Int_Substance_SCTID')
@jwt_required()
def put_update_Int_Substance_SCTID_by_filters():
    """
    The REST method used to update a SNOMED records Int_Substance_SCTID field from within the Flask 
    applications SQLite database, by field filter/s.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        filters = request.json['filters']
        val = request.json['Int_Substance_SCTID']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400
            
        return snomed_schema.jsonify(update_Int_Substance_SCTID_by_filters(filters, val)) 
    except:
        logging.exception('Update SNOMED Int_Substance_SCTID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400   