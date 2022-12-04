from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

@auth.post('/auth')
def post_auth():
    return jsonify({'msg': 'Authentication Endpoint'})