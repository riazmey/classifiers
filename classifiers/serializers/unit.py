
from rest_framework import serializers  
from classifiers.models import Unit

from classifiers.validators import (
    validate_unit_code_dec,
    validate_unit_notation_national,
    validate_unit_notation_international)


class SerializerUnit(serializers.ModelSerializer):
    code_dec = serializers.CharField()
    name = serializers.CharField()
    type = serializers.CharField()
    area_using = serializers.CharField()
    notation_national = serializers.CharField()
    notation_international = serializers.CharField()
    code_national = serializers.CharField()
    code_international = serializers.CharField()
    repr = serializers.CharField()

    class Meta:  
        model = Unit 
        fields = (
            'code_dec',
            'name',
            'type',
            'area_using',
            'notation_national',
            'notation_international',
            'code_national',
            'code_international',
            'repr')


class SerializerUnitCodeDec(serializers.Serializer):
    code_dec = serializers.CharField(validators=[validate_unit_code_dec])


class SerializerUnitNotationNational(serializers.Serializer):
    notation_national = serializers.CharField(validators=[validate_unit_notation_national])


class SerializerUnitNotationInternational(serializers.Serializer):
    notation_international = serializers.CharField(validators=[validate_unit_notation_international])
