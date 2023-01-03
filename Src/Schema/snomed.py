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
    """
    SnomedSchema class represents a schema definition built via the ORM model to enable validation of SQLite table records
    and synchronization between SQLite records and JSON.

    :param ma: The Flask applications schema global for automatic schema building via model definition
    :type ma: SQLAlchemyAutoSchema
    """
    class Meta:
        model = Snomed
        load_instance = True

    MP_PT = fields.Str(required = False)

snomed_schema = SnomedSchema()
"""The Snomed schema global"""

snomeds_schema = SnomedSchema(many = True)
"""The Snomed schema global supporting multiple SQLite records"""