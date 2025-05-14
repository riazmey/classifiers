
from rest_framework import serializers  
from classifiers.models import CargoHazard
from classifiers.validators import validate_cargo_hazard_code_str


class SerializerCargoHazard(serializers.ModelSerializer):
    code_str = serializers.CharField()
    name = serializers.CharField()
    repr = serializers.CharField()

    class Meta:  
        model = CargoHazard 
        fields = (
            'code_str',
            'name',
            'repr')


class SerializerCargoHazardCodeStr(serializers.Serializer):
    code_str = serializers.CharField(validators=[validate_cargo_hazard_code_str])
