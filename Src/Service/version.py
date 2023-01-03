"""
The version service module: Version table services.

Provides the application with the modelled CRUD functionality needed to manage
the version SQLite table.
"""

from Database.database import db
from Model.version import Version
from Schema.version import VersionSchema
from Utils.app_logging import log

@log
def get_version():
    """
    Queries the Version SQLite database table for the applications current AMT
    distribution version record.

    :return: The Version record found within the SQLite database table
    :rtype: Version
    """
    return Version.query.get(1)

@log
def create_version(date, file, link):
    """
    Creates a new Version record within the Version SQLite database table.

    :param date: The version date
    :type date: str
    :param file: The file name
    :type file: str
    :param link: The distribution download URL
    :type link: str
    :return: The newly created Version record
    :rtype: Version
    """
    record = Version(date, file, link)
    db.session.add(record)
    db.session.commit()
    return record

@log
def delete_versions():
    """
    Deletes the applications current Version record found within the SQLite database table.

    :return: The deleted version record
    :rtype: Version
    """
    records = Version.query.delete()
    db.session.commit()
    return records