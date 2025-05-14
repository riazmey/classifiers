
from rest_framework import serializers  
from classifiers.models import RateVAT
from classifiers.validators import validate_rate_vat_code_str


class SerializerRateVAT(serializers.ModelSerializer):
    code_str = serializers.CharField()
    rate = serializers.IntegerField()
    repr = serializers.CharField()

    class Meta:  
        model = RateVAT 
        fields = (
            'code_str',
            'rate',
            'repr')


class SerializerRateVATCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_rate_vat_code_str])
