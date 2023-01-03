import pytest
from app import create_app
from Database.database import db, initalize_db
from config import TestConfig
from datetime import timedelta
from Auth.auth import bcrypt

@pytest.fixture(scope = 'session')
def app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app
        db.drop_all 
        
@pytest.fixture(scope = 'session')
def test_client(app):
    return app.test_client()

@pytest.fixture(scope = 'function')
def clean_database():
    from Model.amt import Amt, Snomed
    from Model.version import Version
    from Model.admin import Admin
    Amt.query.delete()
    Snomed.query.delete()
    Admin.query.delete()
    Version.query.delete()
    db.session.commit()

@pytest.fixture(scope = 'session')
def JWT_token():
    from Service.admin import create_admin
    from flask_jwt_extended import create_access_token
    create_admin('test_admin', bcrypt.generate_password_hash('password'), 'test_email@gmail.com.au')
    return create_access_token({'username': 'test_admin'}, timedelta(minutes=5))