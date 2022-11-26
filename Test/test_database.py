import pytest
import os
from sqlalchemy import inspect

from app import app
from Database.database import db, initalize_db
from Model.admin import Admin
from Model.amt import Amt, Snomed
from Model.version import Version

@pytest.fixture(scope = 'module')
def setup_test_context():
    app.config['Testing'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        initalize_db(app)
        yield app
        db.drop_all()

def test_database_creation():
    model_tables = [Admin.__tablename__, Amt.__tablename__, Snomed.__tablename__, Version.__tablename__]
    db_tables = inspect(db.engine).get_table_names()
    for table in model_tables:
        assert table in db_tables
