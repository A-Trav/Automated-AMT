import pytest
from app import create_app
from Database.database import db, initalize_db

@pytest.fixture(scope = 'session')
def app():
    app = create_app('test_config.cfg')
    with app.app_context():
        yield app
        db.drop_all 
        
@pytest.fixture(scope = 'session')
def test_client(app):
    return app.test_client()