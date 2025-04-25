
from rest_framework import serializers  
from classifiers.models import RateVAT


def RateVATValidateCodeStr(code_str: str):
    try:
        return RateVAT.objects.get(code_str=code_str)
    except RateVAT.DoesNotExist:
        message = f'Couldn\'t find a vat rate with code_str equal to \'{code_str}\''
        raise serializers.ValidationError(message)

class RateVATSerializerData(serializers.ModelSerializer):
    code_str = serializers.CharField()
    rate = serializers.IntegerField()
    repr = serializers.CharField()

    class Meta:  
        model = RateVAT 
        fields = (
            'code_str',
            'rate',
            'repr')

class RateVATGetByCodeStrSerializerParams(serializers.Serializer):
    code_str = serializers.CharField(validators=[RateVATValidateCodeStr])