from flask import Blueprint, request, jsonify
from Schema.amt import amts_schema, amt_schema 
from Schema.snomed import snomed_schema, snomeds_schema 
from Service.search import amt_search_by_id, amt_search_by_fields_ret_all, amt_unmapped_search
from Service.search import snomed_search_by_id,  snomed_search_by_fields_ret_all  

search = Blueprint('search', __name__)

@search.get('/search/amt/id')
def get_amt_search_id():
    try:
        id = request.args['id']
        return amt_schema.jsonify(amt_search_by_id(id)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400        

@search.get('/search/snomed/id')
def get_snomed_search_key():
    try:
        id = request.args['id']
        return snomed_schema.jsonify(snomed_search_by_id(id)) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400   

@search.get('/search/amt')
def get_amt_search():
    try:
        filters = request.json['filters']

        errors = amt_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400

        return amts_schema.jsonify(amt_search_by_fields_ret_all(filters))
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400    

@search.get('/search/snomed')
def get_snomed_search():
    try:
        filters = request.json['filters']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400
            
        return snomeds_schema.jsonify(snomed_search_by_fields_ret_all(filters))
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400     

@search.get('/search/amt/unmapped')
def get_unmapped_amt():
    try:
        return amts_schema.jsonify(amt_unmapped_search()) 
    except:
        return jsonify({'msg': 'The server could not process the request'}), 400      