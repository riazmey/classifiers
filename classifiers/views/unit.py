
from rest_framework.response import Response
from rest_framework.views import APIView
from classifiers.serializers import UnitSerializerData
from classifiers.serializers import UnitGetByCodeDecSerializerParams
from classifiers.serializers import UnitGetByNotationNationalSerializerParams
from classifiers.models import Unit

class UnitAPIView(APIView):

    def get(self, request):

        code_dec = request.query_params.get('code_dec', '')
        notation_national = request.query_params.get('notation_national', '')

        if code_dec:
            params = UnitGetByCodeDecSerializerParams(data=request.query_params)
        elif notation_national:
            params = UnitGetByNotationNationalSerializerParams(data=request.query_params)

        params.is_valid(raise_exception=True)

        if code_dec:
            queryset = Unit.objects.filter(code_dec=code_dec)
        elif notation_national:
            queryset = Unit.objects.filter(notation_national=notation_national)

        if queryset:
            data = queryset[0]

        return Response(UnitSerializerData(data).data)
