
import os
import json

from django.db import transaction
from django.conf import settings
from classifiers.models import Currency
from classifiers.models import Unit
from classifiers.models import RatesVAT


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
            if settings.DEBUG == True:
                if created == True:
                    print(f' Created currency: {data_object.repr}')
                else:
                    print(f' Update currency: {data_object.repr}')
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
            if settings.DEBUG == True:
                if created == True:
                    print(f' Created unit: {data_object.repr}')
                else:
                    print(f' Update unit: {data_object.repr}')
        if settings.DEBUG == True:
            print('')

@transaction.atomic
def filling_rates_vat():
    if settings.DEBUG == True:
        print('Filling VAT rates data:')
    path_file = f'{os.getcwd()}/classifiers/filling/rates_vat.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_str = item_data.get('code_str', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'rate': item_data.get('rate', 0),
                'repr': item_data.get('repr', '')
            }
            data_object, created = RatesVAT.objects.update_or_create(code_str=code_str, defaults=defaults)
            if settings.DEBUG == True:
                if created == True:
                    print(f' Created VAT rate: {data_object.repr}')
                else:
                    print(f' Update VAT rate: {data_object.repr}')
        if settings.DEBUG == True:
            print('')

def filling_all():
    filling_currency()
    filling_unit()
    filling_rates_vat()