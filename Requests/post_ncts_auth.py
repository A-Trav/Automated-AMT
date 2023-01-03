"""
The post_ncts_auth module: NCTS Authentication HTTP Request.

Provides the application with functionality to make a HTTP request
to the NCTS server in-order to retrieve an authentication token.
"""

from flask import jsonify
import requests
import os
from app_logging import log

@log
def get_auth_token():
    req = {
        'grant_type': os.getenv('GRANT_TYPE'), 
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET')
    }
    res = requests.post('https://api.healthterminologies.gov.au/oauth2/token', req)
    res.raise_for_status() # raise exception for any statuscode 400 and greater
    return res