"""
The admin model module: Admin table model.

Provides the applications object relational model for the admin SQLite 
database table.
"""

from Database.database import db

class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email