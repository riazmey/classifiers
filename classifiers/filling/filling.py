
import os
import json

from django.db import transaction
from django.conf import settings
from classifiers.models import Currency
from classifiers.models import Unit

@transaction.atomic
def filling_currency():
    if settings.DEBUG == True:
        print('Filling currency data:')
    path_file = f'{os.getcwd()}/classifiers/filling/currency.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_dec = item_data.get('code_dec', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'code_str': item_data.get('code_str', ''),
                'name': item_data.get('name', '')
            }
            data_object, created = Currency.objects.update_or_create(code_dec=code_dec, defaults=defaults)
            if created | settings.DEBUG == True:
                print(f' Create/update currency: {data_object.repr}')
        if settings.DEBUG == True:
            print('')

@transaction.atomic
def filling_unit():
    if settings.DEBUG == True:
        print('Filling units of measurement:')
    path_file = f'{os.getcwd()}/classifiers/filling/unit.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_dec = item_data.get('code_dec', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'name': item_data.get('name', ''),
                'notation_national': item_data.get('notation_national', ''),
                'notation_international': item_data.get('notation_international', ''),
                'code_national': item_data.get('code_national', ''),
                'code_international': item_data.get('code_international', ''),
                'repr': item_data.get('repr', ''),
            }
            data_object, created = Unit.objects.update_or_create(code_dec=code_dec, defaults=defaults)
            if created | settings.DEBUG == True:
                print(f' Create/update unit: {data_object.repr}')
        if settings.DEBUG == True:
            print('')

def filling_all():
    filling_currency()
    filling_unit()