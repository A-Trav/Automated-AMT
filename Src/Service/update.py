"""
The update service module: Update record services.

Provides the application with the modelled update functionality needed to 
update an existing AMT or Snomed database table record.
"""

from Database.database import db
from Service.search import snomed_search_by_fields_ret_one, snomed_search_by_id
from Model.amt import Snomed
from Utils.app_logging import log

def _AU_Substance_SCTID_update_by_rec(record, value):
    record.AU_Substance_SCTID = value
    db.session.commit()
    return record
    
def _Int_Substance_SCTID_update_by_rec(record, value):
    record.Int_Substance_SCTID = value
    db.session.commit()
    return record

@log
def update_AU_Substance_SCTID_by_filters(filters, value):
    """
    Queries a Snomed record by field filter/s and updates the AU_Substance_SCTID field of a Snomed Record

    :param filters: The field filters to query by
    :type filters: JSON
    :param value: The value to update the AU_Substance_SCTID field to 
    :type value: str
    :return: The updates Snomed record
    :rtype: Snomed
    """
    return _AU_Substance_SCTID_update_by_rec(snomed_search_by_fields_ret_one(filters), value)

@log
def update_AU_Substance_SCTID_by_id(id, value):
    """
    Queries a Snomed record by id (MP_PT) and updates the AU_Substance_SCTID field of a Snomed Record

    :param id: The MP_PT field to query by
    :type id: str
    :param value: The value to update the AU_Substance_SCTID field to 
    :type value: str
    :return: The updates Snomed record
    :rtype: Snomed
    """
    return _AU_Substance_SCTID_update_by_rec(snomed_search_by_id(id), value) 

@log
def update_Int_Substance_SCTID_by_filters(filters, value):
    """
    Queries a Snomed record by field filter/s and updates the Int_Substance_SCTID field of a Snomed Record

    :param filters: The field filters to query by
    :type filters: JSON
    :param value: The value to update the Int_Substance_SCTID field to 
    :type value: str
    :return: The updates Snomed record
    :rtype: Snomed
    """
    return _Int_Substance_SCTID_update_by_rec(snomed_search_by_fields_ret_one(filters), value)

@log
def update_Int_Substance_SCTID_by_id(id, value):
    """
    Queries a Snomed record by id (MP_PT) and updates the Int_Substance_SCTID field of a Snomed Record

    :param id: The MP_PT field to query by
    :type id: str
    :param value: The value to update the Int_Substance_SCTID field to 
    :type value: str
    :return: The updates Snomed record
    :rtype: Snomed
    """
    return _Int_Substance_SCTID_update_by_rec(snomed_search_by_id(id), value) 