import pytest
from datetime import date

from Model.admin import Admin
from Model.amt import Amt, Snomed
from Model.version import Version

def test_admin():
    admin = Admin('test_admin', 'test_password', 'test_email')
    assert admin.id == None
    assert admin.username == 'test_admin'
    assert admin.password == 'test_password'
    assert admin.email == 'test_email'
    
def test_amt():
    amt = Amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
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

    snomed = Snomed('test_field1', 'test_field2', 'test_field3')
    amt.snomed = snomed
    assert amt.snomed.MP_PT == 'test_field1'
    assert amt.snomed.AU_Substance_SCTID == 'test_field2'
    assert amt.snomed.Int_Substance_SCTID == 'test_field3'

def test_snomed():
    snomed = Snomed('test_field1', 'test_field2', 'test_field3')
    assert snomed.MP_PT == 'test_field1'
    assert snomed.AU_Substance_SCTID == 'test_field2'
    assert snomed.Int_Substance_SCTID == 'test_field3'

    amt = Amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    snomed.amt = amt

    assert snomed.amt.CTPP_SCTID == 'test_field1'
    assert snomed.amt.CTPP_PT == 'test_field2'
    assert snomed.amt.ARTG_ID == 'test_field3'
    assert snomed.amt.TPP_SCTID == 'test_field4'
    assert snomed.amt.TPUU_PT == 'test_field5'
    assert snomed.amt.TPP_PT == 'test_field6'
    assert snomed.amt.TPUU_SCTID == 'test_field7'
    assert snomed.amt.TPP_TP_SCTID == 'test_field8'
    assert snomed.amt.TPP_TP_PT == 'test_field9'
    assert snomed.amt.TPUU_TP_SCTID == 'test_field10'
    assert snomed.amt.TPUU_TP_PT == 'test_field11'
    assert snomed.amt.MPP_SCTID == 'test_field12'
    assert snomed.amt.MPP_PT == 'test_field13'
    assert snomed.amt.MPUU_SCTID == 'test_field14'
    assert snomed.amt.MPUU_PT == 'test_field15'
    assert snomed.amt.MP_SCTID == 'test_field16'
    assert snomed.amt.MP_PT == 'test_field17'
    assert snomed.amt.MP_PT == 'test_field17'

def test_version():
    version = Version(str(date.today()), 'test_file.txt', 'test_link')
    assert version.date == str(date.today())
    assert version.file == 'test_file.txt'
    assert version.link == 'test_link'