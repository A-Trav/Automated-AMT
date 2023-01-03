"""
The version schema module: Version table schema.

Provides the applications object relational model schema validation and
synchronization for the version SQLite table. To support the integration of
CRUD functionality with REST API.
"""

from Database.database import ma
from Model.version import Version

class VersionSchema(ma.SQLAlchemyAutoSchema):
    """
    VersionSchema class represents a schema definition built via the ORM model to enable validation of SQLite table records
    and synchronization between SQLite records and JSON.

    :param ma: The Flask applications schema global for automatic schema building via model definition
    :type ma: SQLAlchemyAutoSchema
    """
    class Meta:
        model = Version
        load_instance = True

version_schema = VersionSchema()
"""The Version schema global"""