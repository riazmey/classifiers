
from rest_framework import serializers  
from classifiers.models import Unit


def UnitValidateCodeDec(code_dec: str):
    try:
        return Unit.objects.get(code_dec=code_dec)
    except Unit.DoesNotExist:
        message = f'Couldn\'t find a unit of measurement with code_dec equal to \'{code_dec}\''
        raise serializers.ValidationError(message)

def UnitValidateNotationNational(notation_national: str):
    try:
        return Unit.objects.get(notation_national=notation_national)
    except Unit.DoesNotExist:
        message = f'Couldn\'t find a unit of measurement with notation_national equal to \'{notation_national}\''
        raise serializers.ValidationError(message)

def UnitValidateNotationInternational(notation_international: str):
    try:
        return Unit.objects.get(notation_international=notation_international)
    except Unit.DoesNotExist:
        message = f'Couldn\'t find a unit of measurement with notation_international equal to \'{notation_international}\''
        raise serializers.ValidationError(message)

class UnitSerializerData(serializers.ModelSerializer):
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

class UnitGetByCodeDecSerializerParams(serializers.Serializer):
    code_dec = serializers.CharField(validators=[UnitValidateCodeDec])

class UnitGetByNotationNationalSerializerParams(serializers.Serializer):
    notation_national = serializers.CharField(validators=[UnitValidateNotationNational])

class UnitGetByNotationInternationalSerializerParams(serializers.Serializer):
    notation_international = serializers.CharField(validators=[UnitValidateNotationInternational])