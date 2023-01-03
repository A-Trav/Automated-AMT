"""
The create service module: Create record services.

Provides the application with the modelled create functionality needed to 
construct a new AMT or Snomed database table record.
"""

from Database.database import db
from Model.amt import Amt, Snomed
from app_logging import log

@log
def create_amt(CTPP_SCTID, CTPP_PT, ARTG_ID, TPP_SCTID,
    TPUU_PT, TPP_PT, TPUU_SCTID, TPP_TP_SCTID, TPP_TP_PT,
    TPUU_TP_SCTID, TPUU_TP_PT, MPP_SCTID, MPP_PT, MPUU_SCTID,
    MPUU_PT, MP_SCTID, MP_PT):
    amt = Amt(CTPP_SCTID, CTPP_PT, ARTG_ID, TPP_SCTID,
        TPUU_PT, TPP_PT, TPUU_SCTID, TPP_TP_SCTID, TPP_TP_PT,
        TPUU_TP_SCTID, TPUU_TP_PT, MPP_SCTID, MPP_PT, MPUU_SCTID,
        MPUU_PT, MP_SCTID, MP_PT)
    db.session.add(amt)
    db.session.commit()
    return amt

@log
def create_snomed(MP_PT, AU_Substance_SCTID, Int_Substance_SCTID):
    snomed = Snomed(MP_PT, AU_Substance_SCTID, Int_Substance_SCTID)
    db.session.add(snomed)
    db.session.commit()
    return snomed