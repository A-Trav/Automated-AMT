"""
The snomed schema module: Snomed table schema.

Provides the applications object relational model schema validation and
synchronization for the Snomed SQLite table. To support the integration of
CRUD functionality with REST API.
"""

from marshmallow import fields
from Database.database import ma
from Model.amt import Snomed

class SnomedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Snomed
        load_instance = True

    MP_PT = fields.Str(required = False)

snomed_schema = SnomedSchema()
snomeds_schema = SnomedSchema(many = True)