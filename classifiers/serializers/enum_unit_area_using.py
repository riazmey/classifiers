
from rest_framework import serializers  
from classifiers.validators import validate_enum_unit_area_using_code_str


class SerializerEnumUnitAreaUsingCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_enum_unit_area_using_code_str])
