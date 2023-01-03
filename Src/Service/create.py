"""
The create service module: Create record services.

Provides the application with the modelled create functionality needed to 
construct a new AMT or Snomed database table record.
"""

from Database.database import db
from Model.amt import Amt, Snomed
from Utils.app_logging import log

@log
def create_amt(CTPP_SCTID, CTPP_PT, ARTG_ID, TPP_SCTID,
    TPUU_PT, TPP_PT, TPUU_SCTID, TPP_TP_SCTID, TPP_TP_PT,
    TPUU_TP_SCTID, TPUU_TP_PT, MPP_SCTID, MPP_PT, MPUU_SCTID,
    MPUU_PT, MP_SCTID, MP_PT):
    """
    Creates a new Amt record within the Amt SQLite database table.

    :param CTPP_SCTID: The new Amt records CTPP_SCTID field value 
    :type CTPP_SCTID: str
    :param CTPP_PT: The new Amt records CTPP_PT field value
    :type CTPP_PT: str
    :param ARTG_ID: The new Amt records ARTG_ID field value
    :type ARTG_ID: str
    :param TPP_SCTID: The new Amt records TPP_SCTID field value
    :type TPP_SCTID: str
    :param TPUU_PT: The new Amt records TPUU_PT field value
    :type TPUU_PT: str
    :param TPP_PT: The new Amt records TPP_PT field value
    :type TPP_PT: str
    :param TPUU_SCTID: The new Amt records TPUU_SCTID field value
    :type TPUU_SCTID: str
    :param TPP_TP_SCTID: The new Amt records TPP_TP_SCTID field value
    :type TPP_TP_SCTID: str
    :param TPP_TP_PT: The new Amt records TPP_TP_PT field value
    :type TPP_TP_PT: str
    :param TPUU_TP_SCTID: The new Amt records TPUU_TP_SCTID field value
    :type TPUU_TP_SCTID: str
    :param TPUU_TP_PT: The new Amt records TPUU_TP_PT field value
    :type TPUU_TP_PT: str
    :param MPP_SCTID: The new Amt records MPP_SCTID field value
    :type MPP_SCTID: str
    :param MPP_PT: The new Amt records MPP_PT field value
    :type MPP_PT: str
    :param MPUU_SCTID: The new Amt records MPUU_SCTID field value
    :type MPUU_SCTID: str
    :param MPUU_PT: The new Amt records MPUU_PT field value
    :type MPUU_PT: str
    :param MP_SCTID: The new Amt records MP_SCTID field value
    :type MP_SCTID: str
    :param MP_PT: The new Amt records MP_PT field value
    :type MP_PT: str
    :return: The newly created Amt record
    :rtype: Amt
    """
    amt = Amt(CTPP_SCTID, CTPP_PT, ARTG_ID, TPP_SCTID,
        TPUU_PT, TPP_PT, TPUU_SCTID, TPP_TP_SCTID, TPP_TP_PT,
        TPUU_TP_SCTID, TPUU_TP_PT, MPP_SCTID, MPP_PT, MPUU_SCTID,
        MPUU_PT, MP_SCTID, MP_PT)
    db.session.add(amt)
    db.session.commit()
    return amt

@log
def create_snomed(MP_PT, AU_Substance_SCTID, Int_Substance_SCTID):
    """
    Creates a new Snomed record within the Snomed SQLite database table.

    :param MP_PT: The new Snomed records MP_PT field value
    :type MP_PT: str
    :param AU_Substance_SCTID: The new Snomed records AU_Substance_SCTID field value
    :type AU_Substance_SCTID: str
    :param Int_Substance_SCTID: The new Snomed records Int_Substance_SCTID field value
    :type Int_Substance_SCTID: str
    :return: The newly created Snomed record
    :rtype: Snomed
    """
    snomed = Snomed(MP_PT, AU_Substance_SCTID, Int_Substance_SCTID)
    db.session.add(snomed)
    db.session.commit()
    return snomed