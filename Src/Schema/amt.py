"""
The amt schema module: Amt table schema.

Provides the applications object relational model schema validation and
synchronization for the Amt SQLite table. To support the integration of
CRUD functionality with REST API.
"""

from marshmallow import fields, validate
from Database.database import ma
from Model.amt import Amt
from Schema.snomed import SnomedSchema

class AMTSchema(ma.SQLAlchemyAutoSchema):
    """
    AMTSchema class represents a schema definition built via the ORM model to enable validation of SQLite table records
    and synchronization between SQLite records and JSON.

    :param ma: The Flask applications schema global for automatic schema building via model definition
    :type ma: SQLAlchemyAutoSchema
    """
    class Meta:
        model = Amt
        load_instance = True
    
    ID = fields.Int(required = False)
    snomed = fields.Nested(SnomedSchema, required = False)

amt_schema = AMTSchema()
"""The Amt schema global"""

amts_schema = AMTSchema(many=True)
"""The Amt schema global supporting multiple SQLite records"""