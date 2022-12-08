import requests

def get_distro_csv(url, token):
    res = requests.get(url, headers={'Authorization': token}, stream = True)
    res.raise_for_status() # raise exception for any status 400 and higher
    return res