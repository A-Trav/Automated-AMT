"""
The version schema module: Version table schema.

Provides the applications object relational model schema validation and
synchronization for the version SQLite table. To support the integration of
CRUD functionality with REST API.
"""

from Database.database import ma
from Model.version import Version

class VersionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Version
        load_instance = True

version_schema = VersionSchema()