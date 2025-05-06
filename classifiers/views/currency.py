
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from classifiers.serializers import CurrencySerializerData
from classifiers.serializers import CurrencyGetByCodeDecSerializerParams
from classifiers.serializers import CurrencyGetByCodeStrSerializerParams
from classifiers.models import Currency


class СurrenciesAPIView(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        
        queryset = Currency.objects.all()

        if queryset:
            return Response(CurrencySerializerData(queryset, many=True).data)
        else:
            message = 'Couldn\'t find a currencies'
            raise serializers.ValidationError(message)

class CurrencyAPIView(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        code_dec = request.query_params.get('code_dec', '')
        code_str = request.query_params.get('code_str', '')

        if code_dec:
            params = CurrencyGetByCodeDecSerializerParams(data=request.query_params)
        elif code_str:
            params = CurrencyGetByCodeStrSerializerParams(data=request.query_params)

        params.is_valid(raise_exception=True)

        if code_dec:
            queryset = Currency.objects.filter(code_dec=code_dec)
        elif code_str:
            queryset = Currency.objects.filter(code_str=code_str)

        if queryset:
            data = queryset[0]

        return Response(CurrencySerializerData(data).data)
