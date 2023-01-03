"""
The database module: Database for application.

Provides globals and functionality to support the applications
required SQLite database and ORM modelling.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from Utils.app_logging import log

db = SQLAlchemy()
"""The SQLAlchemy database global"""

ma = Marshmallow()
"""The Marshmallow schema management global"""

@log
def initalize_db(app):
    """
    Creates and integrates the SQLite database with the current Flask application.

    :param app: The current flask application to initialize the database with
    :type app: Flask applicaton
    """
    from Model.amt import Amt, Snomed
    from Model.version import Version
    from Model.admin import Admin
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
