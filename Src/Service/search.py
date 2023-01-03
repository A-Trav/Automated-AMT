"""
The search service module: Search record services.

Provides the application with the modelled search functionality needed to 
query for an AMT or Snomed database table record.
"""

from Database.database import db
from Model.amt import Amt, Snomed
from sqlalchemy import or_
from Utils.app_logging import log

def _amt_build_field_filter(search_filters):
    filters = [getattr(Amt, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Amt.query.filter(*filters)

def _snomed_build_field_filter(search_filters):
    filters = [getattr(Snomed, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Snomed.query.filter(*filters)

@log
def amt_search_by_fields_ret_one(search_filters):
    """
    Queries the Amt SQLite database table by field filter/s

    :param search_filters: The field filter/s to query by
    :type search_filters: JSON
    :return: The retrieved Amt record or None
    :rtype: Amt/None
    """
    return _amt_build_field_filter(search_filters).one_or_none()

@log
def snomed_search_by_fields_ret_one(search_filters):
    """
    Queries the Snomed SQLite database table by field filter/s

    :param search_filters: The field filter/s to query by
    :type search_filters: JSON
    :return: The retrieved Snomed record or None
    :rtype: Snomed/None
    """
    return _snomed_build_field_filter(search_filters).one_or_none()

@log
def amt_search_by_fields_ret_all(search_filters):
    """
    Queries the Amt SQLite database table by field filter/s

    :param search_filters: The field filter/s to query by
    :type search_filters: JSON
    :return: The list containing all retrieved Amt records
    :rtype: list
    """
    return _amt_build_field_filter(search_filters).all()

@log
def snomed_search_by_fields_ret_all(search_filters):
    """
    Queries the Snomed SQLite database table by field filter/s

    :param search_filters: The field filter/s to query by
    :type search_filters: JSON
    :return: The list containing all retrieved Snomed records
    :rtype: list
    """
    return _snomed_build_field_filter(search_filters).all()

@log
def amt_search_by_id(id):
    """
    Queries the Amt SQLite database table by id

    :param id: The ID field value to query for
    :type id: Int
    :return: The Amt record found
    :rtype: Amt
    """
    return Amt.query.get(id)

@log
def snomed_search_by_id(id):
    """
    Queries the Snomed SQLite database table by id (MP_PT)

    :param id: The MP_PT field value to query for
    :type id: str
    :return: The Snomed record found
    :rtype: Snomed
    """
    return Snomed.query.get(id)

@log
def amt_query_all():
    """
    Queries all Amt records from the SQLite database table.

    :return: The list containing all of the Amt records found within the table
    :rtype: list
    """
    return Amt.query.all()

@log
def snomed_query_all():
    """
    Queries all Snomed records from the SQLite database table.

    :return: The list containing all of the Snomed records found within the table
    :rtype: list
    """
    return Snomed.query.all()

@log
def amt_unmapped_search():
    """
    Queries all Amt records from that have no relation mapped to the Snomed SQLite database table.

    :return: The list consisting of all Amt records that have no mapping to the Snomed SQLite database table
    :rtype: Amt
    """    
    return Amt.query.join(Snomed, isouter=True).filter(Snomed.MP_PT == None).all()