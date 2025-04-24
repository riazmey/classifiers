
from rest_framework import serializers  
from classifiers.models import RatesVAT


def RatesVATValidateCodeStr(code_str: str):
    try:
        return RatesVAT.objects.get(code_str=code_str)
    except RatesVAT.DoesNotExist:
        message = f'Couldn\'t find a vat rate with code_str equal to \'{code_str}\''
        raise serializers.ValidationError(message)

class RatesVATSerializerData(serializers.ModelSerializer):
    code_str = serializers.CharField()
    rate = serializers.IntegerField()
    repr = serializers.CharField()

    class Meta:  
        model = RatesVAT 
        fields = (
            'code_str',
            'rate',
            'repr')

class RatesVATGetByCodeStrSerializerParams(serializers.Serializer):
    code_str = serializers.CharField(validators=[RatesVATValidateCodeStr])