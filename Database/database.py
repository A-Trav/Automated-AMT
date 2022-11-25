from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# DB related globals
db = SQLAlchemy()
ma = Marshmallow()

def initalize_db(app):
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    db.session.commit()