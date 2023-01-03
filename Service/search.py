"""
The search service module: Search record services.

Provides the application with the modelled search functionality needed to 
query for an AMT or Snomed database table record.
"""

from Database.database import db
from Model.amt import Amt, Snomed
from sqlalchemy import or_
from app_logging import log

def _amt_build_field_filter(search_filters):
    filters = [getattr(Amt, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Amt.query.filter(*filters)

def _snomed_build_field_filter(search_filters):
    filters = [getattr(Snomed, key).like('%%%s%%' % search_filters[key]) for key in search_filters.keys()]
    return Snomed.query.filter(*filters)

@log
def amt_search_by_fields_ret_one(search_filters):
    return _amt_build_field_filter(search_filters).one_or_none()

@log
def snomed_search_by_fields_ret_one(search_filters):
    return _snomed_build_field_filter(search_filters).one_or_none()

@log
def amt_search_by_fields_ret_all(search_filters):
    return _amt_build_field_filter(search_filters).all()

@log
def snomed_search_by_fields_ret_all(search_filters):
    return _snomed_build_field_filter(search_filters).all()

@log
def amt_search_by_id(id):
    return Amt.query.get(id)

@log
def snomed_search_by_id(id):
    return Snomed.query.get(id)

@log
def amt_query_all():
    return Amt.query.all()

@log
def snomed_query_all():
    return Snomed.query.all()

@log
def amt_unmapped_search():
    return Amt.query.join(Snomed, isouter=True).filter(Snomed.MP_PT == None).all()