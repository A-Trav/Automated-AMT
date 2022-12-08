from flask import Blueprint, request, jsonify
from Schema.amt import amt_schema
from Schema.snomed import snomed_schema
from Service.create import create_amt, create_snomed

create = Blueprint('create', __name__)

@create.post('/create/amt')
def post_amt_create():
    try:
        req = request.json['create']
        error = amt_schema.validate(req)
        
        if len(error) != 0:
            return jsonify(error), 401

        record = create_amt(req['CTPP_SCTID'], req['CTPP_PT'], req['ARTG_ID'], req['TPP_SCTID'],
            req['TPUU_PT'], req['TPP_PT'], req['TPUU_SCTID'], req['TPP_TP_SCTID'], req['TPP_TP_PT'],
            req['TPUU_TP_SCTID'], req['TPUU_TP_PT'], req['MPP_SCTID'], req['MPP_PT'], req['MPUU_SCTID'],
            req['MPUU_PT'], req['MP_SCTID'], req['MP_PT'])
        
        return amt_schema.jsonify(record)
    except Exception as e:
        return jsonify({'msg': 'The server could not process the request'}), 400

@create.post('/create/snomed')
def post_snomed_create():
    try:
        req = request.json['create']
        error = snomed_schema.validate(req)
        
        if len(error) != 0:
            return jsonify(error), 401

        record = create_snomed(req['MP_PT'], req['AU_Substance_SCTID'], req['Int_Substance_SCTID'])
        
        return snomed_schema.jsonify(record)
    except Exception as e:
        return jsonify({'msg': 'The server could not process the request'}), 400