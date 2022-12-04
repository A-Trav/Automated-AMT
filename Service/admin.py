from Database.database import db
from Model.admin import Admin

def get_admin_user_by_username(username):
    return Admin.query.filter_by(username = username).scalar()

def get_admin_user():
    return Admin.query.get(1)

def create_admin(username, password, email):
    admin = Admin(username, password, email)
    db.session.add(admin)
    db.session.commit()

def get_admin_email():
    admin = Admin.query.get(1)
    return admin.email