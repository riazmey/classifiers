
from rest_framework import serializers  
from classifiers.models import LegalType
from classifiers.validators import validate_legal_type_code_str


class SerializerLegalType(serializers.ModelSerializer):

    class Meta:  
        model = LegalType 
        fields = (
            'code_str',
            'name')


class SerializerLegalTypeCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_legal_type_code_str])
