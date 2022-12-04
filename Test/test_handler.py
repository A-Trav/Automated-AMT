import pytest

from Database.database import db
from Test.fixtures import app, test_client
from Service.create import create_amt, create_snomed
from Model.amt import Amt, Snomed

def clear_tables():
    db.session.query(Amt).delete()
    db.session.query(Snomed).delete()
    db.session.commit()

def test_auth_handler(test_client):
    res = test_client.post('/auth')
    assert res.status_code == 200

def test_create_handler(test_client):
    res = test_client.post('/create/amt', json = {
        'create': {
            'CTPP_SCTID': 'test_field1',
            'CTPP_PT': 'test_field2',
            'ARTG_ID': 'test_field3',
            'TPP_SCTID': 'test_field4',
            'TPUU_PT': 'test_field5',
            'TPP_PT': 'test_field6',
            'TPUU_SCTID': 'test_field7',
            'TPP_TP_SCTID': 'test_field8',
            'TPP_TP_PT': 'test_field9',
            'TPUU_TP_SCTID': 'test_field10',
            'TPUU_TP_PT': 'test_field11',
            'MPP_SCTID': 'test_field12',
            'MPP_PT': 'test_field13',
            'MPUU_SCTID': 'test_field14',
            'MPUU_PT': 'test_field15',
            'MP_SCTID': 'test_field16',
            'MP_PT': 'test_field17'
        }
    })

    assert res.status_code == 200
    assert res.json['CTPP_SCTID'] == 'test_field1'
    assert res.json['CTPP_PT'] == 'test_field2'
    assert res.json['ARTG_ID'] == 'test_field3'
    assert res.json['TPP_SCTID'] == 'test_field4'
    assert res.json['TPUU_PT'] == 'test_field5'
    assert res.json['TPP_PT'] == 'test_field6'
    assert res.json['TPUU_SCTID'] == 'test_field7'
    assert res.json['TPP_TP_SCTID'] == 'test_field8'
    assert res.json['TPP_TP_PT'] == 'test_field9'
    assert res.json['TPUU_TP_SCTID'] == 'test_field10'
    assert res.json['TPUU_TP_PT'] == 'test_field11'
    assert res.json['MPP_SCTID'] == 'test_field12'
    assert res.json['MPP_PT'] == 'test_field13'
    assert res.json['MPUU_SCTID'] == 'test_field14'
    assert res.json['MPUU_PT'] == 'test_field15'
    assert res.json['MP_SCTID'] == 'test_field16'
    assert res.json['MP_PT'] == 'test_field17'

    res = test_client.post('/create/snomed', json = {
        'create': {
            'MP_PT': 'test_field1',
            'AU_Substance_SCTID': 'test_field2',
            'Int_Substance_SCTID': 'test_field3'
        }
    })

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'test_field1'
    assert res.json['AU_Substance_SCTID'] == 'test_field2'
    assert res.json['Int_Substance_SCTID'] == 'test_field3'

def test_delete_handler(test_client):
    clear_tables()

    #  /delete/snomed
    snomed = create_snomed('test_field1', 'test_field2', 'test_field3')
    res = test_client.delete('/delete/snomed', json = {
        'filters': {
            'MP_PT': 'test_field1',
            'AU_Substance_SCTID': 'test_field2'
        }
    })

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'test_field1'
    assert res.json['AU_Substance_SCTID'] == 'test_field2'
    assert res.json['Int_Substance_SCTID'] == 'test_field3'

    amt = create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')
    
    # /delete/amt
    res = test_client.delete('/delete/amt', json = {
        'filters': {
            'CTPP_SCTID': 'test_field1',
            'CTPP_PT': 'test_field2'
        }
    })

    assert res.status_code == 200
    assert res.json['CTPP_SCTID'] == 'test_field1'
    assert res.json['CTPP_PT'] == 'test_field2'
    assert res.json['ARTG_ID'] == 'test_field3'
    assert res.json['TPP_SCTID'] == 'test_field4'
    assert res.json['TPUU_PT'] == 'test_field5'
    assert res.json['TPP_PT'] == 'test_field6'
    assert res.json['TPUU_SCTID'] == 'test_field7'
    assert res.json['TPP_TP_SCTID'] == 'test_field8'
    assert res.json['TPP_TP_PT'] == 'test_field9'
    assert res.json['TPUU_TP_SCTID'] == 'test_field10'
    assert res.json['TPUU_TP_PT'] == 'test_field11'
    assert res.json['MPP_SCTID'] == 'test_field12'
    assert res.json['MPP_PT'] == 'test_field13'
    assert res.json['MPUU_SCTID'] == 'test_field14'
    assert res.json['MPUU_PT'] == 'test_field15'
    assert res.json['MP_SCTID'] == 'test_field16'
    assert res.json['MP_PT'] == 'test_field17'

    #  /delete/snomed/id
    snomed = create_snomed('test_field1', 'test_field2', 'test_field3')
    res = test_client.delete('/delete/snomed/id', 
        query_string = {'id': 'test_field1'})

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'test_field1'
    assert res.json['AU_Substance_SCTID'] == 'test_field2'
    assert res.json['Int_Substance_SCTID'] == 'test_field3'
    
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'test_field17')

    #  /delete/amt/id
    res = test_client.delete('/delete/amt/id', 
        query_string = {'id': '1'})

    assert res.status_code == 200
    assert res.json['CTPP_SCTID'] == 'test_field1'
    assert res.json['CTPP_PT'] == 'test_field2'
    assert res.json['ARTG_ID'] == 'test_field3'
    assert res.json['TPP_SCTID'] == 'test_field4'
    assert res.json['TPUU_PT'] == 'test_field5'
    assert res.json['TPP_PT'] == 'test_field6'
    assert res.json['TPUU_SCTID'] == 'test_field7'
    assert res.json['TPP_TP_SCTID'] == 'test_field8'
    assert res.json['TPP_TP_PT'] == 'test_field9'
    assert res.json['TPUU_TP_SCTID'] == 'test_field10'
    assert res.json['TPUU_TP_PT'] == 'test_field11'
    assert res.json['MPP_SCTID'] == 'test_field12'
    assert res.json['MPP_PT'] == 'test_field13'
    assert res.json['MPUU_SCTID'] == 'test_field14'
    assert res.json['MPUU_PT'] == 'test_field15'
    assert res.json['MP_SCTID'] == 'test_field16'
    assert res.json['MP_PT'] == 'test_field17'

def test_export_handler(test_client):
    res = test_client.get('/export')
    assert res.status_code == 200

def test_search_handler(test_client):
    clear_tables()

    snomed = create_snomed('snomed_test_field1', 'snomed_test_field2', 'snomed_test_field3')
    create_amt('test_field1', 'test_field2', 'test_field3', 'test_field4', 'test_field5', 
            'test_field6', 'test_field7', 'test_field8', 'test_field9', 'test_field10', 
            'test_field11', 'test_field12', 'test_field13', 'test_field14', 'test_field15',
            'test_field16', 'snomed_test_field1')

    #  /search/amt/id
    res = test_client.get('/search/amt/id', 
        query_string = {'id': '1'})

    assert res.status_code == 200
    assert res.json['CTPP_SCTID'] == 'test_field1'
    assert res.json['CTPP_PT'] == 'test_field2'
    assert res.json['ARTG_ID'] == 'test_field3'
    assert res.json['TPP_SCTID'] == 'test_field4'
    assert res.json['TPUU_PT'] == 'test_field5'
    assert res.json['TPP_PT'] == 'test_field6'
    assert res.json['TPUU_SCTID'] == 'test_field7'
    assert res.json['TPP_TP_SCTID'] == 'test_field8'
    assert res.json['TPP_TP_PT'] == 'test_field9'
    assert res.json['TPUU_TP_SCTID'] == 'test_field10'
    assert res.json['TPUU_TP_PT'] == 'test_field11'
    assert res.json['MPP_SCTID'] == 'test_field12'
    assert res.json['MPP_PT'] == 'test_field13'
    assert res.json['MPUU_SCTID'] == 'test_field14'
    assert res.json['MPUU_PT'] == 'test_field15'
    assert res.json['MP_SCTID'] == 'test_field16'
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['snomed']['MP_PT'] == 'snomed_test_field1'
    assert res.json['snomed']['AU_Substance_SCTID'] == 'snomed_test_field2' 
    assert res.json['snomed']['Int_Substance_SCTID'] == 'snomed_test_field3'

    #  /search/snomed/id
    res = test_client.get('/search/snomed/id', 
        query_string = {'id': 'snomed_test_field1'})
    
    assert res.status_code == 200
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['AU_Substance_SCTID'] == 'snomed_test_field2'
    assert res.json['Int_Substance_SCTID'] == 'snomed_test_field3'

    #  /search/amt
    res = test_client.get('/search/amt', json = {
        'filters': {
            'CTPP_SCTID': 'test_field1',
            'CTPP_PT': 'test_field2',
        }
    })

    assert res.status_code == 200
    assert len(res.json) == 1
    assert res.json[0]['CTPP_SCTID'] == 'test_field1'
    assert res.json[0]['CTPP_PT'] == 'test_field2'
    assert res.json[0]['ARTG_ID'] == 'test_field3'
    assert res.json[0]['TPP_SCTID'] == 'test_field4'
    assert res.json[0]['TPUU_PT'] == 'test_field5'
    assert res.json[0]['TPP_PT'] == 'test_field6'
    assert res.json[0]['TPUU_SCTID'] == 'test_field7'
    assert res.json[0]['TPP_TP_SCTID'] == 'test_field8'
    assert res.json[0]['TPP_TP_PT'] == 'test_field9'
    assert res.json[0]['TPUU_TP_SCTID'] == 'test_field10'
    assert res.json[0]['TPUU_TP_PT'] == 'test_field11'
    assert res.json[0]['MPP_SCTID'] == 'test_field12'
    assert res.json[0]['MPP_PT'] == 'test_field13'
    assert res.json[0]['MPUU_SCTID'] == 'test_field14'
    assert res.json[0]['MPUU_PT'] == 'test_field15'
    assert res.json[0]['MP_SCTID'] == 'test_field16'
    assert res.json[0]['MP_PT'] == 'snomed_test_field1'
    assert res.json[0]['snomed']['MP_PT'] == 'snomed_test_field1'
    assert res.json[0]['snomed']['AU_Substance_SCTID'] == 'snomed_test_field2' 
    assert res.json[0]['snomed']['Int_Substance_SCTID'] == 'snomed_test_field3'

    # /search/snomed
    res = test_client.get('/search/snomed', json = {
        'filters': {
            'AU_Substance_SCTID': 'snomed_test_field2',
            'Int_Substance_SCTID': 'snomed_test_field3',
        }
    })

    assert res.status_code == 200
    assert res.json[0]['MP_PT'] == 'snomed_test_field1'
    assert res.json[0]['AU_Substance_SCTID'] == 'snomed_test_field2'
    assert res.json[0]['Int_Substance_SCTID'] == 'snomed_test_field3'


def test_update_handler(test_client):
    clear_tables()

    snomed = create_snomed('snomed_test_field1', 'snomed_test_field2', 'snomed_test_field3')

    # /update/snomed/AU_Substance_SCTID/id
    res = test_client.put('/update/snomed/AU_Substance_SCTID/id', 
        query_string = {'id': 'snomed_test_field1'}, 
        json = {'AU_Substance_SCTID': 'new_snomed_test_field2'}
    )

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['AU_Substance_SCTID'] == 'new_snomed_test_field2'
    assert res.json['Int_Substance_SCTID'] == 'snomed_test_field3'

    # /update/snomed/AU_Substance_SCTID
    res = test_client.put('/update/snomed/AU_Substance_SCTID', json = {
        'AU_Substance_SCTID': 'snomed_test_field2',
        'filters': {
            'AU_Substance_SCTID': 'new_snomed_test_field2',
            'Int_Substance_SCTID': 'snomed_test_field3',
        }
    })

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['AU_Substance_SCTID'] == 'snomed_test_field2'
    assert res.json['Int_Substance_SCTID'] == 'snomed_test_field3'

    # /update/snomed/Int_Substance_SCTID/id
    res = test_client.put('/update/snomed/Int_Substance_SCTID/id', 
        query_string = {'id': 'snomed_test_field1'},
        json = {'Int_Substance_SCTID': 'new_snomed_test_field3'}
    )

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['AU_Substance_SCTID'] == 'snomed_test_field2'
    assert res.json['Int_Substance_SCTID'] == 'new_snomed_test_field3'

    # /update/snomed/Int_Substance_SCTID
    res = test_client.put('/update/snomed/Int_Substance_SCTID', json = {
        'Int_Substance_SCTID': 'snomed_test_field3',
        'filters': {
            'AU_Substance_SCTID': 'snomed_test_field2',
            'Int_Substance_SCTID': 'snomed_test_field3',
        }
    })

    assert res.status_code == 200
    assert res.json['MP_PT'] == 'snomed_test_field1'
    assert res.json['AU_Substance_SCTID'] == 'snomed_test_field2'
    assert res.json['Int_Substance_SCTID'] == 'snomed_test_field3'

