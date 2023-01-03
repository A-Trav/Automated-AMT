"""
The http module: HTTP request utilities.

Provides functionality to process the received responses from HTTP requests 
sent by the application in order to integrate with the NCTS Server.
"""

import atoma, requests

def response_to_csv(http_response, file_name): 
    if (http_response.headers['content-type'] == 'text/csv'):
        csv_file = open(file_name, "wb")
        for chunk in http_response.iter_content(chunk_size = None):
            if chunk:
                csv_file.write(chunk)
        csv_file.close()

def xml_response_to_version(http_response):
    if (http_response.headers['content-type'] == 'application/xml'):
        versions = dict()
        feed = atoma.parse_atom_bytes(http_response.content)
        for entry in feed.entries:
            if entry.categories[0].term == 'AMT_CSV':
                date = entry.published
                link = entry.links[0].href
                file_name = link.split('/').pop()
                versions[date] = {'file_name': file_name, 'link': link}
        
        return versions