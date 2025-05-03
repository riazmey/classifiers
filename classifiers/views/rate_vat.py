
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from classifiers.serializers import RateVATSerializerData
from classifiers.serializers import RateVATGetByCodeStrSerializerParams
from classifiers.models import RateVAT


class RatesVATAPIView(APIView):

    def get(self, request):
        
        queryset = RateVAT.objects.all()

        if queryset:
            return Response(RateVATSerializerData(queryset, many=True).data)
        else:
            message = 'Couldn\'t find a rates VAT'
            raise serializers.ValidationError(message)

class RateVATAPIView(APIView):

    def get(self, request):

        code_str = request.query_params.get('code_str', '')
        params = RateVATGetByCodeStrSerializerParams(data=request.query_params)
        params.is_valid(raise_exception=True)

        queryset = RateVAT.objects.filter(code_str=code_str)

        if queryset:
            data = queryset[0]

        return Response(RateVATSerializerData(data).data)
