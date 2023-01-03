"""
The version model module: Version table model.

Provides the applications object relational model for the version SQLite 
database table.
"""

from Database.database import db

class Version(db.Model):
    __tablename__ = 'Version'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String, nullable=False,)
    file = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, Date, File, Link):
        self.date = Date
        self.file = File
        self.link = Link