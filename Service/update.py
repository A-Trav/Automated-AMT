"""
The update service module: Update record services.

Provides the application with the modelled update functionality needed to 
update an existing AMT or Snomed database table record.
"""

from Database.database import db
from Service.search import snomed_search_by_fields_ret_one, snomed_search_by_id
from Model.amt import Snomed
from app_logging import log

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
    return _AU_Substance_SCTID_update_by_rec(snomed_search_by_fields_ret_one(filters), value)

@log
def update_AU_Substance_SCTID_by_id(id, value):
    return _AU_Substance_SCTID_update_by_rec(snomed_search_by_id(id), value) 

@log
def update_Int_Substance_SCTID_by_filters(filters, value):
    return _Int_Substance_SCTID_update_by_rec(snomed_search_by_fields_ret_one(filters), value)

@log
def update_Int_Substance_SCTID_by_id(id, value):
    return _Int_Substance_SCTID_update_by_rec(snomed_search_by_id(id), value) 