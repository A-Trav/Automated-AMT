from Database.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

class Snomed(Base, db.Model):
    __tablename__ = 'Snomed'
    MP_PT = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    AU_Substance_SCTID = db.Column(db.String, nullable=True)
    Int_Substance_SCTID = db.Column(db.String, nullable=True)

    def __init__(self, MP_PT, AU_Substance_SCTID, Int_Substance_SCTID):
        self.MP_PT = MP_PT
        self.AU_Substance_SCTID = AU_Substance_SCTID
        self.Int_Substance_SCTID = Int_Substance_SCTID

class Amt(Base, db.Model):
    __tablename__ = 'Amt'
    ID = db.Column(db.Integer, primary_key=True, nullable=False)
    CTPP_SCTID = db.Column(db.String, nullable=True)
    CTPP_PT = db.Column(db.String, nullable=True)
    ARTG_ID = db.Column(db.String, nullable=True)
    TPP_SCTID = db.Column(db.String, nullable=True)
    TPUU_PT = db.Column(db.String, nullable=True)
    TPP_PT = db.Column(db.String, nullable=True)
    TPUU_SCTID = db.Column(db.String, nullable=True)
    TPP_TP_SCTID = db.Column(db.String, nullable=True)
    TPP_TP_PT = db.Column(db.String, nullable=True)
    TPUU_TP_SCTID = db.Column(db.String, nullable=True)
    TPUU_TP_PT = db.Column(db.String, nullable=True)
    MPP_SCTID = db.Column(db.String, nullable=True)
    MPP_PT = db.Column(db.String, nullable=True)
    MPUU_SCTID = db.Column(db.String, nullable=True)
    MPUU_PT = db.Column(db.String, nullable=True)
    MP_SCTID = db.Column(db.String, nullable=True)
    MP_PT = db.Column(db.String, nullable=True) 
    Snomed = db.Column(db.String, ForeignKey('Snomed.MP_PT', ondelete='CASCADE'), nullable=True)

    def __init__(self, CTPP_SCTID, CTPP_PT, ARTG_ID, TPP_SCTID,
        TPUU_PT, TPP_PT, TPUU_SCTID, TPP_TP_SCTID, TPP_TP_PT,
        TPUU_TP_SCTID, TPUU_TP_PT, MPP_SCTID, MPP_PT, MPUU_SCTID,
        MPUU_PT, MP_SCTID, MP_PT):
        self.CTPP_SCTID = CTPP_SCTID
        self.CTPP_PT = CTPP_PT
        self.ARTG_ID = ARTG_ID
        self.TPP_SCTID = TPP_SCTID
        self.TPUU_PT = TPUU_PT
        self.TPP_PT = TPP_PT
        self.TPUU_SCTID = TPUU_SCTID
        self.TPP_TP_SCTID = TPP_TP_SCTID
        self.TPP_TP_PT = TPP_TP_PT
        self.TPUU_TP_SCTID = TPUU_TP_SCTID
        self.TPUU_TP_PT = TPUU_TP_PT
        self.MPP_SCTID = MPP_SCTID
        self.MPP_PT = MPP_PT
        self.MPUU_SCTID = MPUU_SCTID
        self.MPUU_PT = MPUU_PT
        self.MP_SCTID = MP_SCTID
        self.MP_PT = MP_PT
        self.Snomed = MP_PT

Base.prepare()