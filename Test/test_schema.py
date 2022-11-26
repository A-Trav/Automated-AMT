import pytest
from flask import jsonify, json
from datetime import date

from app import app
from Model.admin import Admin
from Schema.admin import admin_schema
from Model.amt import Amt, Snomed
from Schema.amt import amt_schema
from Schema.snomed import snomed_schema
from Model.version import Version
from Schema.version import version_schema

@pytest.fixture(scope = 'module')
def setup_test_context():
    app.config['Testing'] = True
    yield app


def check_no_error_occurs(error_list):
    assert len(error_list) == 0

def check_error_occurs(error_list):
    assert len(error_list) != 0 

def test_admin():
    check_no_error_occurs(admin_schema.validate({
        'username': 'test_user', 
        'password': 'test_password', 
        'email': 'test_email@hotmail.com'
    }))

    check_no_error_occurs(admin_schema.validate({
        'username': 'test_user', 
        'password': 'test_password', 
    }))

    # Check valid fields defined
    check_error_occurs(admin_schema.validate({'password': 'test_password', 'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user',  'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({}))

    # check username validation
    check_error_occurs(admin_schema.validate({'username': 'test', 'password': 'test_password', 'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({'username': 12345678, 'password': 'test_password', 'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({'username': 123456.78, 'password': 'test_password', 'email': 'test_email@hotmail.com'}))

    # check password validation
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test', 'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 12345678, 'email': 'test_email@hotmail.com'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 123456.78, 'email': 'test_email@hotmail.com'}))

    # check email validation
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': 'test'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': 'test_email'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': '@test_email'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': 'user@test_email'}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': 12345678}))
    check_error_occurs(admin_schema.validate({'username': 'test_user', 'password': 'test_password', 'email': 123456.78}))

    schema_json = admin_schema.jsonify(Admin('test_user', 'test_password', 'test_email@hotmail.com'))
    assert schema_json.json['username'] == 'test_user'
    assert schema_json.json['password'] == 'test_password'
    assert schema_json.json['email'] == 'test_email@hotmail.com'

def test_amt():

    check_no_error_occurs(amt_schema.validate({
        'CTPP_SCTID': 'test_field1',
        'CTPP_PT': 'test_field2',
        'ARTG_ID': 'test_field3',
        'TPP_SCTID': 'test_field4',
        'TPUU_PT': 'test_field5',
        'TPP_PT': 'test_field6',
        'TPUU_SCTID': 'test_field7',
        'TPP_TP_SCTID': 'test_field8',
        'TPP_TP_PT': 'test_field9',
        'TPUU_TP_SCTID': 'test_field9',
        'TPUU_TP_PT': 'test_field10',
        'MPP_SCTID': 'test_field11',
        'MPP_PT': 'test_field12',
        'MPUU_SCTID': 'test_field13',
        'MPUU_PT': 'test_field14',
        'MP_SCTID': 'test_field15',
        'MP_PT': 'test_field16',
    }))

    check_no_error_occurs(amt_schema.validate({
        'MP_PT': 'test_field16'
    }))
    
    check_error_occurs(amt_schema.validate({
        'ID': 1,
        'CTPP_SCTID': 'test_field1',
        'CTPP_PT': 'test_field2',
        'ARTG_ID': 'test_field3',
        'TPP_SCTID': 'test_field4',
        'TPUU_PT': 'test_field5',
        'TPP_PT': 'test_field6',
        'TPUU_SCTID': 'test_field7',
        'TPP_TP_SCTID': 'test_field8',
        'TPP_TP_PT': 'test_field9',
        'TPUU_TP_SCTID': 'test_field9',
        'TPUU_TP_PT': 'test_field10',
        'MPP_SCTID': 'test_field11',
        'MPP_PT': 'test_field12',
        'MPUU_SCTID': 'test_field13',
        'MPUU_PT': 'test_field14',
        'MP_SCTID': 'test_field15',
    }))
    
    amt = Amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')

    schema_json = amt_schema.jsonify(amt)
    
    assert schema_json.json['CTPP_SCTID'] == 'test_field1'
    assert schema_json.json['CTPP_PT'] == 'test_field2'
    assert schema_json.json['ARTG_ID'] == 'test_field3'
    assert schema_json.json['TPP_SCTID'] == 'test_field4'
    assert schema_json.json['TPUU_PT'] == 'test_field5'
    assert schema_json.json['TPP_PT'] == 'test_field6'
    assert schema_json.json['TPUU_SCTID'] == 'test_field7'
    assert schema_json.json['TPP_TP_SCTID'] == 'test_field8'
    assert schema_json.json['TPP_TP_PT'] == 'test_field9'
    assert schema_json.json['TPUU_TP_SCTID'] == 'test_field10'
    assert schema_json.json['TPUU_TP_PT'] == 'test_field11'
    assert schema_json.json['MPP_SCTID'] == 'test_field12'
    assert schema_json.json['MPP_PT'] == 'test_field13'
    assert schema_json.json['MPUU_SCTID'] == 'test_field14'
    assert schema_json.json['MPUU_PT'] == 'test_field15'
    assert schema_json.json['MP_SCTID'] == 'test_field16'
    assert schema_json.json['MP_PT'] == 'test_field17'
    assert schema_json.json['snomed'] == None

    amt.snomed = Snomed('test_field1', 'test_field2', 'test_field3')
    schema_json = amt_schema.jsonify(amt)

    assert schema_json.json['CTPP_SCTID'] == 'test_field1'
    assert schema_json.json['CTPP_PT'] == 'test_field2'
    assert schema_json.json['ARTG_ID'] == 'test_field3'
    assert schema_json.json['TPP_SCTID'] == 'test_field4'
    assert schema_json.json['TPUU_PT'] == 'test_field5'
    assert schema_json.json['TPP_PT'] == 'test_field6'
    assert schema_json.json['TPUU_SCTID'] == 'test_field7'
    assert schema_json.json['TPP_TP_SCTID'] == 'test_field8'
    assert schema_json.json['TPP_TP_PT'] == 'test_field9'
    assert schema_json.json['TPUU_TP_SCTID'] == 'test_field10'
    assert schema_json.json['TPUU_TP_PT'] == 'test_field11'
    assert schema_json.json['MPP_SCTID'] == 'test_field12'
    assert schema_json.json['MPP_PT'] == 'test_field13'
    assert schema_json.json['MPUU_SCTID'] == 'test_field14'
    assert schema_json.json['MPUU_PT'] == 'test_field15'
    assert schema_json.json['MP_SCTID'] == 'test_field16'
    assert schema_json.json['MP_PT'] == 'test_field17'
    assert type(schema_json.json['snomed']) == dict
    assert schema_json.json['snomed']['MP_PT'] == 'test_field1'
    assert schema_json.json['snomed']['AU_Substance_SCTID'] == 'test_field2'
    assert schema_json.json['snomed']['Int_Substance_SCTID'] == 'test_field3'

def test_snomed():

    check_no_error_occurs(snomed_schema.validate({
        'MP_PT': 'test_field1',
        'AU_Substance_SCTID': 'test_field2',
        'Int_Substance_SCTID': 'test_field3',
    }))

    check_error_occurs(snomed_schema.validate({
        'AU_Substance_SCTID': 'test_field2',
        'Int_Substance_SCTID': 'test_field3',
    }))

    snomed = Snomed('test_field1', 'test_field2', 'test_field3')
    schema_json = snomed_schema.jsonify(snomed)
    assert schema_json.json['MP_PT'] == 'test_field1'
    assert schema_json.json['AU_Substance_SCTID'] == 'test_field2'
    assert schema_json.json['Int_Substance_SCTID'] == 'test_field3'
    with pytest.raises(Exception):
        schema_json.json['amt']  == None  # Not a valid field in the Snomed Schema

def test_version():

    check_no_error_occurs(version_schema.validate({
        'date': str(date.today()),
        'file': 'test_file.txt',
        'link': 'www.test_link.com'
    }))

    check_error_occurs(version_schema.validate({
        'file': 'test_file.txt',
        'link': 'www.test_link.com'
    }))

    check_error_occurs(version_schema.validate({
        'date': str(date.today()),
        'link': 'www.test_link.com'
    }))

    check_error_occurs(version_schema.validate({
        'date': str(date.today()),
        'file': 'test_file.txt',
    }))

    version = Version(str(date.today()), 'test_file.txt', 'test_link')
    schema_json = version_schema.jsonify(version)

    assert schema_json.json['date'] == str(date.today())
    assert schema_json.json['file'] == 'test_file.txt'
    assert schema_json.json['link'] == 'test_link'