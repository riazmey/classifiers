
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from classifiers.models import (
    Unit,
    EnumUnitType,
    EnumUnitAreaUsing)

from classifiers.serializers import (
    SerializerUnit,
    SerializerUnitType,
    SerializerUnitAreaUsing,
    SerializerUnitCodeDec,
    SerializerUnitNotationNational,
    SerializerUnitNotationInternational)


class APIViewOKEI(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        available_fields = [
            'code_dec',
            'type',
            'area_using',
            'notation_national',
            'notation_international']

        query_params = {**request.query_params}

        if query_params:
            for key, value in query_params.items():
                serializer_params = None
                value = query_params[key][0]
                if not key in available_fields:
                    message = f'Unknown parameter "{key}".'
                    raise serializers.ValidationError(message)
                elif key == 'type':
                    serializer_params = SerializerUnitType(data=request.query_params)
                    if serializer_params.is_valid(raise_exception=True):
                        value = EnumUnitType.objects.get(code_str=value)
                elif key == 'area_using':
                    serializer_params = SerializerUnitAreaUsing(data=request.query_params)
                    if serializer_params.is_valid(raise_exception=True):
                        value = EnumUnitAreaUsing.objects.get(code_str=value)
                elif key == 'code_dec':
                    serializer_params = SerializerUnitCodeDec(data=request.query_params)
                elif key == 'notation_national':
                    serializer_params = SerializerUnitNotationNational(data=request.query_params)
                elif key == 'notation_international':
                    serializer_params = SerializerUnitNotationInternational(data=request.query_params)
                query_params[key] = value
                if serializer_params:
                    serializer_params.is_valid(raise_exception=True)

        queryset = Unit.objects.filter(**query_params)

        if queryset:
            return Response(SerializerUnit(queryset, many=True).data)
        else:
            if query_params:
                message = f'Couldn\'t find a units of measurement with params: {query_params}'
            else:
                message = f'There are no entries in the unit classifier in the database.'
            raise serializers.ValidationError(message)
