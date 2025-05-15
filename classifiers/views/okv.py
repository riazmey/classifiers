
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from classifiers.models import Currency

from classifiers.serializers import (
    SerializerCurrency,
    SerializerCurrencyCodeDec,
    SerializerCurrencyCodeStr)


class APIViewOKV(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        available_fields = [
            'code_dec',
            'code_str']

        query_params = {**request.query_params}

        if query_params:
            for key, value in query_params.items():
                serializer_params = None
                value = query_params[key][0]
                if not key in available_fields:
                    message = f'Unknown parameter "{key}".'
                    raise serializers.ValidationError(message)
                elif key == 'code_dec':
                    serializer_params = SerializerCurrencyCodeDec(data=request.query_params)
                elif key == 'code_str':
                    serializer_params = SerializerCurrencyCodeStr(data=request.query_params)
                query_params[key] = value
                if serializer_params:
                    serializer_params.is_valid(raise_exception=True)

        queryset = Currency.objects.filter(**query_params)

        if queryset:
            return Response(SerializerCurrency(queryset, many=True).data)
        else:
            if query_params:
                message = f'Couldn\'t find a currencies with params: {query_params}'
            else:
                message = f'There are no entries in the currencies classifier in the database.'
            raise serializers.ValidationError(message)
