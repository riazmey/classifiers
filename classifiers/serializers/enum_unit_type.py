
from rest_framework import serializers  
from classifiers.validators import validate_enum_unit_type_code_str


class SerializerEnumUnitTypeCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_enum_unit_type_code_str])
