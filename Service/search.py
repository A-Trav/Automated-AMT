from Database.database import db
from Model.amt import Amt, Snomed
from sqlalchemy import or_

def _amt_build_field_filter(search_filters):
    filters = [getattr(Amt, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Amt.query.filter(*filters)

def _snomed_build_field_filter(search_filters):
    filters = [getattr(Snomed, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Snomed.query.filter(*filters)

def amt_search_by_fields_ret_one(search_filters):
    return _amt_build_field_filter(search_filters).one_or_none()

def snomed_search_by_fields_ret_one(search_filters):
    return _snomed_build_field_filter(search_filters).one_or_none()

def amt_search_by_fields_ret_all(search_filters):
    return _amt_build_field_filter(search_filters).all()

def snomed_search_by_fields_ret_all(search_filters):
    return _snomed_build_field_filter(search_filters).all()

def amt_search_by_id(id):
    return Amt.query.get(id)

def snomed_search_by_id(id):
    return Snomed.query.get(id)

def amt_unmapped_search():
    return Amt.query.join(Snomed, isouter=True).filter(Snomed.MP_PT == None).all()