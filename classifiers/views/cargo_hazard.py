
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from classifiers.models import CargoHazard

from classifiers.serializers import (
    SerializerCargoHazard,
    SerializerCargoHazardCodeStr)


class APIViewCargoHazard(APIView):

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def get(self, request):

        available_fields = ['code_str']
        query_params = {**request.query_params}

        if query_params:
            for key, value in query_params.items():
                serializer_params = None
                value = query_params[key][0]
                if not key in available_fields:
                    message = f'Unknown parameter "{key}".'
                    raise serializers.ValidationError(message)
                elif key == 'code_str':
                    serializer_params = SerializerCargoHazardCodeStr(data=request.query_params)
                query_params[key] = value
                if serializer_params:
                    serializer_params.is_valid(raise_exception=True)

        queryset = CargoHazard.objects.filter(**query_params)

        if queryset:
            return Response(SerializerCargoHazard(queryset, many=True).data)
        else:
            message = 'Couldn\'t find a cargos hazards'
            raise serializers.ValidationError(message)
