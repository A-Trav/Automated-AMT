import pytest
from flask import jsonify
from datetime import date

from Test.fixtures import app
from Database.database import db
from Service.admin import get_admin_user_by_username, get_admin_user, create_admin, get_admin_email
from Service.create import create_amt, create_snomed
from Service.delete import amt_delete_by_id, amt_delete_by_filter
from Service.delete import snomed_delete_by_id, snomed_delete_by_filter
from Service.search import amt_search_by_id, amt_search_by_fields_ret_one, amt_search_by_fields_ret_all 
from Service.search import snomed_search_by_id, snomed_search_by_fields_ret_one, snomed_search_by_fields_ret_all
from Service.update import update_AU_Substance_SCTID_by_filters, update_AU_Substance_SCTID_by_id
from Service.update import update_Int_Substance_SCTID_by_filters, update_Int_Substance_SCTID_by_id
from Service.version import get_version, create_version, delete_versions
from Model.amt import Amt, Snomed

def clear_tables():
    db.session.query(Amt).delete()
    db.session.query(Snomed).delete()
    db.session.commit()

def test_admin_service(app):
    assert get_admin_user() == None
    create_admin('test_admin', 'test_password', 'test_email@hotmail.com')

    admin = get_admin_user_by_username('test_admin')
    assert admin != None
    assert admin.username == 'test_admin'
    assert admin.password == 'test_password'
    assert admin.email == 'test_email@hotmail.com'

    admin = get_admin_user()
    assert admin != None
    assert admin.username == 'test_admin'
    assert admin.password == 'test_password'
    assert admin.email == 'test_email@hotmail.com'

    email = get_admin_email()
    assert email == 'test_email@hotmail.com'

def test_create_service(app):
    clear_tables()
    assert len(Amt.query.all()) == 0
    assert len(Snomed.query.all()) == 0

    amt = create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed == None

    snomed = create_snomed('test_field17', 'snomed_test_field1', 'snomed_test_field2') 
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

def test_delete_service(app):
    clear_tables()
    assert len(Amt.query.all()) == 0
    assert len(Snomed.query.all()) == 0

    create_snomed('test_field17', 'snomed_test_field1', 'snomed_test_field2') 
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    amt = amt_delete_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'
    
    # Ensure no mutation occurs to the snomed record
    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    assert amt_search_by_id(1) == None

    snomed = snomed_delete_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    assert snomed_search_by_id('test_field17') == None

    create_snomed('test_field17', 'snomed_test_field1', 'snomed_test_field2') 
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')

    assert snomed_search_by_id('test_field17') != None 
    assert amt_search_by_id(1) != None

    snomed = snomed_delete_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    assert snomed_search_by_id('test_field17') == None

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed == None

    assert amt_delete_by_id(1) != None
    assert amt_search_by_id(1) == None

def test_search_service(app):
    clear_tables()
    assert len(Amt.query.all()) == 0
    assert len(Snomed.query.all()) == 0

    create_snomed('test_field17', 'snomed_test_field1', 'snomed_test_field2') 
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    create_amt('second_test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    create_amt('third_test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')

    filters = {'CTPP_SCTID': 'second_test_field1'}
    amt = amt_search_by_fields_ret_one(filters)
    assert amt.CTPP_SCTID == 'second_test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    filters = {'MP_PT': 'test_field17'}
    with pytest.raises(Exception):
        amt = amt_search_by_fields_ret_one(filters)

    filters = {'CTPP_PT': 'test_field2', 'MP_PT':'test_field17'}
    amts = amt_search_by_fields_ret_all(filters)
    assert len(amts) == 3
    for amt in amts:
        assert amt.CTPP_PT == 'test_field2'
        assert amt.ARTG_ID == 'test_field3'
        assert amt.TPP_SCTID == 'test_field4'
        assert amt.TPUU_PT == 'test_field5'
        assert amt.TPP_PT == 'test_field6'
        assert amt.TPUU_SCTID == 'test_field7'
        assert amt.TPP_TP_SCTID == 'test_field8'
        assert amt.TPP_TP_PT == 'test_field9'
        assert amt.TPUU_TP_SCTID == 'test_field10'
        assert amt.TPUU_TP_PT == 'test_field11'
        assert amt.MPP_SCTID == 'test_field12'
        assert amt.MPP_PT == 'test_field13'
        assert amt.MPUU_SCTID == 'test_field14'
        assert amt.MPUU_PT == 'test_field15'
        assert amt.MP_SCTID == 'test_field16'
        assert amt.MP_PT == 'test_field17'
        assert amt.snomed != None
        assert amt.snomed.MP_PT == 'test_field17'
        assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
        assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'
    
    create_snomed('second_test_field17', 'snomed_test_field1', 'snomed_test_field2')     
    create_snomed('third_test_field17', 'snomed_test_field1', 'snomed_test_field2')     
    
    filters = {'MP_PT': 'second_test_field17'}
    snomed = snomed_search_by_fields_ret_one(filters)
    assert snomed.MP_PT == 'second_test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    filters = {'AU_Substance_SCTID': 'snomed_test_field1'}
    with pytest.raises(Exception):
        snomed = snomed_search_by_fields_ret_one(filters)
    
    filters = {'AU_Substance_SCTID': 'snomed_test_field1', 'Int_Substance_SCTID': 'snomed_test_field2'}
    snomeds = snomed_search_by_fields_ret_all(filters)
    assert len(snomeds) == 3
    for snomed in snomeds:
        assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
        assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

def test_update_service(app):
    clear_tables()
    assert len(Amt.query.all()) == 0
    assert len(Snomed.query.all()) == 0

    create_snomed('test_field17', 'snomed_test_field1', 'snomed_test_field2') 
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = update_AU_Substance_SCTID_by_id('test_field17', 'new_snomed_test_field1')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'new_snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'new_snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'new_snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    filters = {'Int_Substance_SCTID': 'snomed_test_field2'}
    snomed = update_AU_Substance_SCTID_by_filters(filters, 'snomed_test_field1')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'

    snomed = update_Int_Substance_SCTID_by_id('test_field17', 'new_snomed_test_field2')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'new_snomed_test_field2'

    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'new_snomed_test_field2'

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'new_snomed_test_field2'

    filters = {'AU_Substance_SCTID': 'snomed_test_field1'}
    snomed = update_Int_Substance_SCTID_by_filters(filters, 'snomed_test_field2')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'
    
    snomed = snomed_search_by_id('test_field17')
    assert snomed.MP_PT == 'test_field17'
    assert snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert snomed.Int_Substance_SCTID == 'snomed_test_field2'

    amt = amt_search_by_id(1)
    assert amt.CTPP_SCTID == 'test_field1'
    assert amt.CTPP_PT == 'test_field2'
    assert amt.ARTG_ID == 'test_field3'
    assert amt.TPP_SCTID == 'test_field4'
    assert amt.TPUU_PT == 'test_field5'
    assert amt.TPP_PT == 'test_field6'
    assert amt.TPUU_SCTID == 'test_field7'
    assert amt.TPP_TP_SCTID == 'test_field8'
    assert amt.TPP_TP_PT == 'test_field9'
    assert amt.TPUU_TP_SCTID == 'test_field10'
    assert amt.TPUU_TP_PT == 'test_field11'
    assert amt.MPP_SCTID == 'test_field12'
    assert amt.MPP_PT == 'test_field13'
    assert amt.MPUU_SCTID == 'test_field14'
    assert amt.MPUU_PT == 'test_field15'
    assert amt.MP_SCTID == 'test_field16'
    assert amt.MP_PT == 'test_field17'
    assert amt.snomed != None
    assert amt.snomed.MP_PT == 'test_field17'
    assert amt.snomed.AU_Substance_SCTID == 'snomed_test_field1'
    assert amt.snomed.Int_Substance_SCTID == 'snomed_test_field2'
    
def test_version_service(app):
    assert get_version() == None

    version = create_version(str(date.today()), 'test_file.txt', 'test_link')
    assert version.date == str(date.today())
    assert version.file == 'test_file.txt'
    assert version.link == 'test_link'

    version = get_version()
    assert version.date == str(date.today())
    assert version.file == 'test_file.txt'
    assert version.link == 'test_link'

    version == delete_versions()
    assert version.date == str(date.today())
    assert version.file == 'test_file.txt'
    assert version.link == 'test_link'

    version = get_version()
    assert version == None


