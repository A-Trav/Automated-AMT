"""
The admin schema module: Admin table schema.

Provides the applications object relational model schema validation and
synchronization for the admin SQLite table. To support the integration of
CRUD functionality with REST API.
"""

from marshmallow import fields, validate, Schema 
from Database.database import ma
from Model.admin import Admin

class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Admin
        load_instance = True
    
    username = fields.Str(required = True, validate = validate.Length(min=8))
    password = fields.Str(required = True, validate = validate.Length(min=8))
    email = fields.Email(required = False, validate = [validate.Length(min=8), validate.Email()])

admin_schema = AdminSchema()