"""
The bootstrap_admin module: Admin user construction.

Provides functionality to create an admin user for the application.
"""

from Database.database import db
from Auth.auth import bcrypt
from Schema.admin import admin_schema
from Service.admin import create_admin, delete_admin, get_admin_user 

def bootstrap_admin(app, force_bootstrap):
    with app.app_context():
        if force_bootstrap or get_admin_user() == None:
            delete_admin()
            print('Creating Admin user...') 
            while True:
                username = input('Admin username: ')
                password = input('Admin password: ')
                email = input('Admin email: ')
                errors = admin_schema.validate({'username': username, 'password': password, 'email': email})
                if len(errors) == 0:
                    break 
                print('Invalid admin credentials, username and password must be 8 characters long and email address must be valid')
            create_admin(username, bcrypt.generate_password_hash(password), email)

