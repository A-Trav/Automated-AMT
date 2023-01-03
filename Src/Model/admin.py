"""
The admin model module: Admin table model.

Provides the applications object relational model for the admin SQLite 
database table.
"""

from Database.database import db

class Admin(db.Model):
    """
    Admin class represents an ORM model for the Flask applications admin
    SQLite database table.

    :param db: The Flask applications SQLite database
    :type db: SQLAlchemy
    """
    __tablename__ = 'Admin'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email