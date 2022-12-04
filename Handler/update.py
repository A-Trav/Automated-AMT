from flask import Blueprint, request, jsonify
from Service.update import update_AU_Substance_SCTID_by_id, update_AU_Substance_SCTID_by_filters
from Service.update import update_Int_Substance_SCTID_by_id, update_Int_Substance_SCTID_by_filters
from Schema.snomed import snomed_schema

update = Blueprint('update', __name__)

@update.put('/update/snomed/AU_Substance_SCTID/id')
def put_update_AU_Substance_SCTID_by_id():
    try:
        id = request.args['id']
        val = request.json['AU_Substance_SCTID']
        return snomed_schema.jsonify(update_AU_Substance_SCTID_by_id(id, val)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/AU_Substance_SCTID')
def put_update_AU_Substance_SCTID_by_filters():
    try:
        filters = request.json['filters']
        val = request.json['AU_Substance_SCTID']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400

        return snomed_schema.jsonify(update_AU_Substance_SCTID_by_filters(filters, val)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/Int_Substance_SCTID/id')
def put_update_Int_Substance_SCTID_by_id():
    try:
        id = request.args['id']
        val = request.json['Int_Substance_SCTID']
        return snomed_schema.jsonify(update_Int_Substance_SCTID_by_id(id, val)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400   

@update.put('/update/snomed/Int_Substance_SCTID')
def put_update_Int_Substance_SCTID_by_filters():
    try:
        filters = request.json['filters']
        val = request.json['Int_Substance_SCTID']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400
            
        return snomed_schema.jsonify(update_Int_Substance_SCTID_by_filters(filters, val)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400   