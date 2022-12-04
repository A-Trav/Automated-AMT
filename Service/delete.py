from Database.database import db
from Model.amt import Amt, Snomed
from Service.search import amt_search_by_id, snomed_search_by_id
from Service.search import amt_search_by_fields_ret_one, snomed_search_by_fields_ret_one

def _delete_by_rec(record):
    db.session.delete(record)
    db.session.commit()
    return record

def amt_delete_by_id(id):
    return _delete_by_rec(amt_search_by_id(id))

def snomed_delete_by_id(id):
    return _delete_by_rec(snomed_search_by_id(id))

def amt_delete_by_filter(filters):
    return _delete_by_rec(amt_search_by_fields_ret_one(filters))

def snomed_delete_by_filter(filters):
    return _delete_by_rec(snomed_search_by_fields_ret_one(filters))