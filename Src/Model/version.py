"""
The version model module: Version table model.

Provides the applications object relational model for the version SQLite 
database table.
"""

from Database.database import db

class Version(db.Model):
    """
    Version class represents an ORM model for the Flask applications version
    SQLite database table.

    :param db: The Flask applications SQLite database
    :type db: SQLAlchemy
    """
    __tablename__ = 'Version'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.String, nullable=False,)
    file = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, Date, File, Link):
        self.date = Date
        self.file = File
        self.link = Link