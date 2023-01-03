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
    """
    AdminSchema class represents a schema definition built via the ORM model to enable validation of SQLite table records
    and synchronization between SQLite records and JSON.

    :param ma: The Flask applications schema global for automatic schema building via model definition
    :type ma: SQLAlchemyAutoSchema
    """
    class Meta:
        model = Admin
        load_instance = True
    
    username = fields.Str(required = True, validate = validate.Length(min=8))
    password = fields.Str(required = True, validate = validate.Length(min=8))
    email = fields.Email(required = False, validate = [validate.Length(min=8), validate.Email()])

admin_schema = AdminSchema()
"""The Admin schema global"""