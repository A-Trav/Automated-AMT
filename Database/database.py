"""
The database module: Database for application.

Provides globals and functionality to support the applications
required SQLite database and ORM modelling.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app_logging import log

db = SQLAlchemy()
ma = Marshmallow()

@log
def initalize_db(app):
    from Model.amt import Amt, Snomed
    from Model.version import Version
    from Model.admin import Admin
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
