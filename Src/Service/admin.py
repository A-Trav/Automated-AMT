"""
The admin service module: Admin table services.

Provides the application with the modelled CRUD functionality needed to manage
the admin SQLite table.
"""

from Database.database import db
from Model.admin import Admin
from Utils.app_logging import log

@log
def get_admin_user_by_username(username):
    """
    Retrieves the applications admin user by username, queried from the admin SQLite database table.

    :param username: The applications admin username 
    :type username: str
    :return: The applications admin user
    :rtype: Admin
    """
    return Admin.query.filter_by(username = username).scalar()

@log
def get_admin_user():
    """
    Retrieves the applications admin user, queried from the admin SQLite database table.

    :return: The applications admin user
    :rtype: Admin
    """
    return Admin.query.get(1)

@log
def create_admin(username, password, email):
    """
    Create an Admin record within the applications Admin SQLite database table.

    :param username: The admins username
    :type username: str
    :param password: The admins password, this is expected to be encrypted prior to this function call
    :type password: str
    :param email: The admins email address
    :type email: str
    """
    admin = Admin(username, password, email)
    db.session.add(admin)
    db.session.commit()

@log
def delete_admin():
    """
    Deletes the applications admin user by clearing all records from the Admin SQLite database table
    """
    Admin.query.delete()
    db.session.commit()

@log
def get_admin_email():
    """
    Retrieves the applications admin users email address, queried from the admin SQLite database table.

    :return: The admins email address
    :rtype: str
    """
    admin = Admin.query.get(1)
    return admin.email