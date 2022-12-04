from flask import Blueprint, request, jsonify

export = Blueprint('export', __name__)

@export.get('/export')
def get_export():
    return jsonify({'msg': 'export endpoint'})