"""
The admin service module: Admin table services.

Provides the application with the modelled CRUD functionality needed to manage
the admin SQLite table.
"""

from Database.database import db
from Model.admin import Admin
from app_logging import log

@log
def get_admin_user_by_username(username):
    return Admin.query.filter_by(username = username).scalar()

@log
def get_admin_user():
    return Admin.query.get(1)

@log
def create_admin(username, password, email):
    admin = Admin(username, password, email)
    db.session.add(admin)
    db.session.commit()

@log
def delete_admin():
    Admin.query.delete()
    db.session.commit()

@log
def get_admin_email():
    admin = Admin.query.get(1)
    return admin.email