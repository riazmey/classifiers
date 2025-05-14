
from rest_framework import serializers  
from classifiers.models import Currency

from classifiers.validators import (
    validate_currency_code_dec,
    validate_currency_code_str)


class SerializerCurrency(serializers.ModelSerializer):
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


class SerializerCurrencyCodeDec(serializers.Serializer):
    code_dec = serializers.CharField(validators=[validate_currency_code_dec])


class SerializerCurrencyCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_currency_code_str])
