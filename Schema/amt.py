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
    class Meta:
        model = Amt
        load_instance = True
    
    ID = fields.Int(required = False)
    snomed = fields.Nested(SnomedSchema, required = False)

amt_schema = AMTSchema()
amts_schema = AMTSchema(many=True)