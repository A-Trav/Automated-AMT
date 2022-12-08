import requests

def get_distro_meta():
    res = requests.get('https://api.healthterminologies.gov.au/syndication/v1/syndication.xml')
    res.raise_for_status() # throw exception for any status 400 or higher
    return res