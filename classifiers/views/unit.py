
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from classifiers.serializers import (
    UnitSerializerData,
    UnitGetByCodeDecSerializerParams,
    UnitGetByNotationNationalSerializerParams,
    UnitGetByNotationInternationalSerializerParams)

from classifiers.models import (
    Unit,
    EnumUnitType,
    EnumUnitAreaUsing)


class UnitAPIView(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        available_fields = [
            'code_dec',
            'notation_national',
            'notation_international']

        if len(request.query_params) == 0:
            message = f'The selection parameters were not passed to the request. ' \
                f'Available selection parameters: {', '.join(available_fields)}'
            raise serializers.ValidationError(message)

        code_dec = request.query_params.get('code_dec', '')
        notation_national = request.query_params.get('notation_national', '')
        notation_international = request.query_params.get('notation_international', '')

        if code_dec:
            params = UnitGetByCodeDecSerializerParams(data=request.query_params)
        elif notation_national:
            params = UnitGetByNotationNationalSerializerParams(data=request.query_params)
        elif notation_international:
            params = UnitGetByNotationInternationalSerializerParams(data=request.query_params)

        params.is_valid(raise_exception=True)

        if code_dec:
            queryset = Unit.objects.filter(code_dec=code_dec)
        elif notation_national:
            queryset = Unit.objects.filter(notation_national=notation_national)
        elif notation_international:
            queryset = Unit.objects.filter(notation_international=notation_international)

        if queryset:
            data = queryset[0]
        
        return Response(UnitSerializerData(data).data)


class UnitsAPIView(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        available_fields = [
            'code_dec',
            'type',
            'area_using',
            'notation_national',
            'notation_international',
        ]

        query_params = {**request.query_params}

        if len(query_params) == 0:
            message = f'The selection parameters were not passed to the request. ' \
                f'Available selection parameters: {', '.join(available_fields)}'
            raise serializers.ValidationError(message)
        else:
            for key, value in query_params.items():
                value = query_params[key][0]
                if not key in available_fields:
                    message = f'Unknown parameter "{key}".'
                    raise serializers.ValidationError(message)
                elif key == 'type':
                    value = EnumUnitType.objects.get(code_str=value)
                elif key == 'area_using':
                    value = EnumUnitAreaUsing.objects.get(code_str=value)
                query_params[key] = value

        queryset = Unit.objects.filter(**query_params)

        if queryset:
            return Response(UnitSerializerData(queryset, many=True).data)
        else:
            message = f'Couldn\'t find a unit of measurement with params: {query_params}'
            raise serializers.ValidationError(message)
