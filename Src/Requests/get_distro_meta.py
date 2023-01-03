"""
The get_distro_meta module: Amt Distribution meta HTTP Request.

Provides the application with functionality to make a HTTP request
to the NCTS server, to retrieve metadata on all available distribution imports.
"""

import requests
from Utils.app_logging import log

@log
def get_distro_meta():
    """
    Sends a HTTP request to the NCTS API in order to retrieve an XML response, showing all available
    distributions for import.

    :return: The HTTP requests response
    :rtype: Response
    """
    res = requests.get('https://api.healthterminologies.gov.au/syndication/v1/syndication.xml')
    res.raise_for_status() # throw exception for any status 400 or higher
    return res