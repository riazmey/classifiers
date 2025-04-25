
from rest_framework.response import Response
from rest_framework.views import APIView
from classifiers.serializers import CargoHazardSerializerData
from classifiers.serializers import CargoHazardGetByCodeStrSerializerParams
from classifiers.models import CargoHazard

class CargoHazardAPIView(APIView):

    def get(self, request):

        code_str = request.query_params.get('code_str', '')
        params = CargoHazardGetByCodeStrSerializerParams(data=request.query_params)
        params.is_valid(raise_exception=True)

        queryset = CargoHazard.objects.filter(code_str=code_str)

        if queryset:
            data = queryset[0]

        return Response(CargoHazardSerializerData(data).data)
