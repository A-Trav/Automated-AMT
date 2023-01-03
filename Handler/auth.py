"""
The auth handler module: Authentication endpoint.

Provides the applications authentication REST method for admin authentication
and admin clients JWT retrieval.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, decode_token
from datetime import timedelta
import logging
from Auth.auth import bcrypt, jwt
from Service.admin import get_admin_user_by_username
from Schema.admin import admin_schema
from Handler.create import create

auth = Blueprint('auth', __name__)

@auth.post('/auth')
def post_auth():
    try:
        if not request.authorization: 
            return jsonify({'msg': 'Server could not locate an authorization header with admin credentials'}), 400 
        
        username = request.authorization.username
        password = request.authorization.password

        error = admin_schema.validate({'username': username, 'password': password})
        if len(error) != 0:
            return jsonify(error), 401

        user = get_admin_user_by_username(username)
        if not user: return jsonify({'error': 'Invalid admin credentials'}), 400
        if bcrypt.check_password_hash(user.password, password):
            token = create_access_token({'username': user.username}, timedelta(minutes=30))
            return jsonify({'access_token': token}), 200
        return jsonify({'msg': 'Invalid admin credentials'}), 400
    except:
        logging.exception('Auth handler failure')
        return jsonify({'msg': 'The server could not process the request'}), 400