"""
The get_distro_csv module: Amt Distribution HTTP Request.

Provides the application with functionality to make a HTTP request
to the NCTS server, to download the AMT distribution CSV.
"""

import requests
from app_logging import log

@log
def get_distro_csv(url, token):
    res = requests.get(url, headers={'Authorization': token}, stream = True)
    res.raise_for_status() # raise exception for any status 400 and higher
    return res