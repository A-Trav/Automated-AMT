"""
The delete handler module: Delete endpoint.

Provides the applications delete REST methods for deleting database records
from both the Snomed and Amt SQLite tables.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Schema.amt import amt_schema
from Schema.snomed import snomed_schema
from Schema.amt import AMTSchema
from Service.delete import amt_delete_by_id, amt_delete_by_filter
from Service.delete import snomed_delete_by_id, snomed_delete_by_filter
import logging

delete = Blueprint('delete', __name__)

@delete.delete('/delete/amt/id')
@jwt_required()
def delete_amt_by_id():
    try:
        id = request.args['id']
        schema = AMTSchema(exclude=('snomed',))         
        return schema.jsonify(amt_delete_by_id(id)) 
    except:
        logging.exception('Delete AMT by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400

@delete.delete('/delete/snomed/id')
@jwt_required()
def delete_snomed_by_key():
    try:
        id = request.args['id']
        return snomed_schema.jsonify(snomed_delete_by_id(id)) 
    except:
        logging.exception('Delete SNOMED by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400

@delete.delete('/delete/amt')
@jwt_required()
def delete_amt_by_filter():
    try:
        filters = request.json['filters']
        errors = amt_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400
        
        schema = AMTSchema(exclude=('snomed',))     
        return schema.jsonify(amt_delete_by_filter(filters)) 
    except:
        logging.exception('Delete AMT handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400

@delete.delete('/delete/snomed')
@jwt_required()
def delete_snomed_by_filter():
    try:
        filters = request.json['filters']
        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400

        return snomed_schema.jsonify(snomed_delete_by_filter(filters)) 
    except:
        logging.exception('Delete SNOMED handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400