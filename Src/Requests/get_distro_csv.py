"""
The get_distro_csv module: Amt Distribution HTTP Request.

Provides the application with functionality to make a HTTP request
to the NCTS server, to download the AMT distribution CSV.
"""

import requests
from Utils.app_logging import log

@log
def get_distro_csv(url, token):
    """
    Sends a HTTP request to the provided NCTS URL in order to retrieve the data distribution CSV.

    :param url: The NCTS API URL to import the distribution from
    :type url: str
    :param token: NCTS API client authentication token
    :type token: str
    :return: The HTTP requests response
    :rtype: Response
    """
    res = requests.get(url, headers={'Authorization': token}, stream = True)
    res.raise_for_status() # raise exception for any status 400 and higher
    return res