
from rest_framework import serializers  
from classifiers.models import CargoHazard


def CargoHazardValidateCodeStr(code_str: str):
    try:
        return CargoHazard.objects.get(code_str=code_str)
    except CargoHazard.DoesNotExist:
        message = f'Couldn\'t find a class cargo hazard with code_str equal to \'{code_str}\''
        raise serializers.ValidationError(message)

class CargoHazardSerializerData(serializers.ModelSerializer):
    code_str = serializers.CharField()
    name = serializers.CharField()
    repr = serializers.CharField()

    class Meta:  
        model = CargoHazard 
        fields = (
            'code_str',
            'name',
            'repr')

class CargoHazardGetByCodeStrSerializerParams(serializers.Serializer):
    code_str = serializers.CharField(validators=[CargoHazardValidateCodeStr])