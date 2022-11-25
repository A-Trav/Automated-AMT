
from Database.database import ma
from Model.amt import Snomed

class SnomedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Snomed
        load_instance = True

snomed_schema = SnomedSchema()
snomeds_schema = SnomedSchema(many = True)