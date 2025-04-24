
from rest_framework.response import Response
from rest_framework.views import APIView
from classifiers.serializers import RatesVATSerializerData
from classifiers.serializers import RatesVATGetByCodeStrSerializerParams
from classifiers.models import RatesVAT

class RatesVATAPIView(APIView):

    def get(self, request):

        code_str = request.query_params.get('code_str', '')
        params = RatesVATGetByCodeStrSerializerParams(data=request.query_params)
        params.is_valid(raise_exception=True)

        queryset = RatesVAT.objects.filter(code_str=code_str)

        if queryset:
            data = queryset[0]

        return Response(RatesVATSerializerData(data).data)
