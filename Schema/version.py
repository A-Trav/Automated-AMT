from Database.database import ma
from Model.version import Version

class VersionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Version
        load_instance = True

version_schema = VersionSchema()