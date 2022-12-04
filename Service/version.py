from Database.database import db
from Model.version import Version
from Schema.version import VersionSchema

def get_version():
    return Version.query.get(1)

def create_version(date, file, link):
    record = Version(date, file, link)
    db.session.add(record)
    db.session.commit()
    return record

def delete_versions():
    records = Version.query.delete()
    db.session.commit()
    return records