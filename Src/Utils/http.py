"""
The http module: HTTP request utilities.

Provides functionality to process the received responses from HTTP requests 
sent by the application in order to integrate with the NCTS Server.
"""

import atoma, requests

def response_to_csv(http_response, file_name): 
    """
    Retrieves and downloads the given CSV file from a HTTP request response

    :param http_response: The response object to retrieve the CSV file from
    :type http_response: Response
    :param file_name: The file name to save the CSV file as
    :type file_name: str
    """
    if (http_response.headers['content-type'] == 'text/csv'):
        csv_file = open(file_name, "wb")
        for chunk in http_response.iter_content(chunk_size = None):
            if chunk:
                csv_file.write(chunk)
        csv_file.close()

def xml_response_to_version(http_response):
    """
    Converts the NCTS API available distribution response in to a easily passable dictionary
    consisting of only the available AMT distributions.

    :param http_response: The response object to retrieve the CSV file from
    :type http_response: Response
    :return: A dictionary representation of all available AMT distribution
    :rtype: dict
    """
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