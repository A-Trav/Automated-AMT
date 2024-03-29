"""
The search handler module: Search endpoint.

Provides the applications search REST methods for querying the Snomed and Amt
SQLite tables based on primary key or field filters.
"""

from flask import Blueprint, request, jsonify
from Schema.amt import amts_schema, amt_schema 
from Schema.snomed import snomed_schema, snomeds_schema 
from Service.search import amt_search_by_id, amt_search_by_fields_ret_all, amt_unmapped_search
from Service.search import snomed_search_by_id,  snomed_search_by_fields_ret_all  
import logging

search = Blueprint('search', __name__)
"""The search endpoint blueprint"""

@search.get('/search/amt/id')
def get_amt_search_id():
    """
    The REST method used to query AMT records from within the Flask applications SQLite database,
    by ID.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        id = request.args['id']
        return amt_schema.jsonify(amt_search_by_id(id)) 
    except:
        logging.exception('Search AMT by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400        

@search.get('/search/snomed/id')
def get_snomed_search_key():
    """
    The REST method used to query Snomed records from within the Flask applications SQLite database,
    by primary key.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        id = request.args['id']
        return snomed_schema.jsonify(snomed_search_by_id(id)) 
    except:
        logging.exception('Search SNOMED by ID handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400   

@search.get('/search/amt')
def get_amt_search():
    """
    The REST method used to query AMT records from within the Flask applications SQLite database,
    by field filter/s.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        filters = request.json['filters']

        errors = amt_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400

        return amts_schema.jsonify(amt_search_by_fields_ret_all(filters))
    except:
        logging.exception('search AMT handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400    

@search.get('/search/snomed')
def get_snomed_search():
    """
    The REST method used to query SNOMED records from within the Flask applications SQLite database,
    by field filter/s.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        filters = request.json['filters']

        errors = snomed_schema.validate(filters)

        if len(errors) != 0:
            return jsonify({'msg': 'Invalid filters in request'}), 400
            
        return snomeds_schema.jsonify(snomed_search_by_fields_ret_all(filters))
    except:
        logging.exception('Search SNOMED handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400     

@search.get('/search/amt/unmapped')
def get_unmapped_amt():
    """
    The REST method used to query AMT records from within the Flask applications SQLite database,
    that have no foreign key mapping to the SNOMED SQLite database table.

    :return: The REST methods JSON response and response code
    :rtype: JSON, Int
    """
    try:
        return amts_schema.jsonify(amt_unmapped_search()) 
    except:
        logging.exception('Search AMT unmapped handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400      