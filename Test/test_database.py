import pytest
from sqlalchemy import inspect

from Test.fixtures import app
from Database.database import db
from Model.admin import Admin
from Model.amt import Amt, Snomed
from Model.version import Version

def test_database_creation(app):
    model_tables = [Admin.__tablename__, Amt.__tablename__, Snomed.__tablename__, Version.__tablename__]
    db_tables = inspect(db.engine).get_table_names()
    for table in model_tables:
        assert table in db_tables
