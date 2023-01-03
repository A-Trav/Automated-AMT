"""
The version service module: Version table services.

Provides the application with the modelled CRUD functionality needed to manage
the version SQLite table.
"""

from Database.database import db
from Model.version import Version
from Schema.version import VersionSchema
from app_logging import log

@log
def get_version():
    return Version.query.get(1)

@log
def create_version(date, file, link):
    record = Version(date, file, link)
    db.session.add(record)
    db.session.commit()
    return record

@log
def delete_versions():
    records = Version.query.delete()
    db.session.commit()
    return records