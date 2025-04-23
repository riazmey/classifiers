
from rest_framework import serializers  
from classifiers.models import Currency


def CurrencyValidateCodeDec(code_dec: str):
    try:
        return Currency.objects.get(code_dec=code_dec)
    except Currency.DoesNotExist:
        message = f'Couldn\'t find a currency with code_dec equal to \'{code_dec}\''
        raise serializers.ValidationError(message)

def CurrencyValidateCodeStr(code_str: str):
    try:
        return Currency.objects.get(code_str=code_str)
    except Currency.DoesNotExist:
        message = f'Couldn\'t find a currency with code_str equal to \'{code_str}\''
        raise serializers.ValidationError(message)

class CurrencySerializerData(serializers.ModelSerializer):
    code_dec = serializers.CharField()
    code_str = serializers.CharField()
    name = serializers.CharField()
    repr = serializers.CharField()

    class Meta:  
        model = Currency 
        fields = (
            'code_dec',
            'code_str',
            'name',
            'repr')

class CurrencyGetByCodeDecSerializerParams(serializers.Serializer):
    code_dec = serializers.CharField(validators=[CurrencyValidateCodeDec])

class CurrencyGetByCodeStrSerializerParams(serializers.Serializer):
    code_str = serializers.CharField(validators=[CurrencyValidateCodeStr])