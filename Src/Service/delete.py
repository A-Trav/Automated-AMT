"""
The delete service module: Delete record services.

Provides the application with the modelled delete functionality needed to 
delete an AMT or Snomed database table record.
"""

from Database.database import db
from Model.amt import Amt, Snomed
from Service.search import amt_search_by_id, snomed_search_by_id
from Service.search import amt_search_by_fields_ret_one, snomed_search_by_fields_ret_one
from Utils.app_logging import log

def _delete_by_rec(record):
    db.session.delete(record)
    db.session.commit()
    return record

@log
def amt_delete_by_id(id):
    """
    Deletes an Amt record from the SQLite database table by ID.

    :param id: The ID field to query by
    :type id: Int
    :return: The deleted Amt record
    :rtype: Amt
    """
    return _delete_by_rec(amt_search_by_id(id))

@log
def snomed_delete_by_id(id):
    """
    Deletes a Snomed record from the SQLite database table by ID.

    :param id: The ID field to query by
    :type id: Int
    :return: The deleted Snomed record
    :rtype: Snomed
    """
    return _delete_by_rec(snomed_search_by_id(id))

@log
def amt_delete_by_filter(filters):
    """
    Deletes an Amt record from the SQLite database table by field filter/s.

    :param filters: The field filters to query by
    :type filters: JSON
    :return: The deleted Amt record
    :rtype: Amt
    """
    return _delete_by_rec(amt_search_by_fields_ret_one(filters))

@log
def snomed_delete_by_filter(filters):
    """
    Deletes a Snomed record from the SQLite database table by field filter/s.

    :param filters: The field filters to query by
    :type filters: JSON
    :return: The deleted Snomed record
    :rtype: Snomed
    """
    return _delete_by_rec(snomed_search_by_fields_ret_one(filters))