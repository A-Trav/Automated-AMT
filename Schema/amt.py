from marshmallow import fields, validate
from Database.database import ma
from Model.amt import Amt
from Schema.snomed import SnomedSchema

class AMTSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Amt
        load_instance = True

    MP_PT = fields.Str(required = True, validate = validate.Length(min=2))
    snomed = fields.Nested(SnomedSchema, required = False)

amt_schema = AMTSchema()
amts_schema = AMTSchema(many=True)