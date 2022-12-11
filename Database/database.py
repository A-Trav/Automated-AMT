from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# DB related globals
db = SQLAlchemy()
ma = Marshmallow()

def initalize_db(app):
    from Model.amt import Amt, Snomed
    from Model.version import Version
    from Model.admin import Admin
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()
