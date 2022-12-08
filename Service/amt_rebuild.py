from Database.database import db
from Model.amt import Amt

def delete_amt_table():
    Amt.query.delete()
    db.session.commit()

def rebuild_table_from_dict(dist):
    db.session.bulk_insert_mappings(Amt, dist)
    db.session.commit()