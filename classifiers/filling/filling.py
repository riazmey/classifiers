
import os
import json

from django.db import transaction
from classifiers.models import EnumUnitAreaUsing
from classifiers.models import EnumUnitType
from classifiers.models import Currency
from classifiers.models import Unit
from classifiers.models import RateVAT
from classifiers.models import CargoHazard


@transaction.atomic
def filling_enum_unit_area_using():
    print('Filling enumerate area using units:')
    path_file = f'{os.getcwd()}/classifiers/filling/enum_unit_area_using.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_str = item_data.get('code_str', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'repr': item_data.get('repr', '')
            }
            data_object, created = EnumUnitAreaUsing.objects.update_or_create(code_str=code_str, defaults=defaults)
            if created == True:
                print(f' Created area using unit: {data_object.repr}')
            else:
                print(f' Update area using unit: {data_object.repr}')
        print('')

@transaction.atomic
def filling_enum_unit_type():
    print('Filling enumerate unit types:')
    path_file = f'{os.getcwd()}/classifiers/filling/enum_unit_type.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_str = item_data.get('code_str', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'repr': item_data.get('repr', '')
            }
            data_object, created = EnumUnitType.objects.update_or_create(code_str=code_str, defaults=defaults)
            if created == True:
                print(f' Created unit type: {data_object.repr}')
            else:
                print(f' Update unit type: {data_object.repr}')
        print('')

@transaction.atomic
def filling_currency():
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
            if created == True:
                print(f' Created currency: {data_object.repr}')
            else:
                print(f' Update currency: {data_object.repr}')
        print('')

@transaction.atomic
def filling_unit():
    print('Filling units of measurement:')
    path_file = f'{os.getcwd()}/classifiers/filling/unit.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_dec = item_data.get('code_dec', '')
            type = item_data.get('type', '')
            area_using = item_data.get('area_using', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'name': item_data.get('name', ''),
                'type': EnumUnitType.objects.get(code_str=type),
                'area_using': EnumUnitAreaUsing.objects.get(code_str=area_using),
                'notation_national': item_data.get('notation_national', ''),
                'notation_international': item_data.get('notation_international', ''),
                'code_national': item_data.get('code_national', ''),
                'code_international': item_data.get('code_international', ''),
                'repr': item_data.get('repr', ''),
            }
            data_object, created = Unit.objects.update_or_create(code_dec=code_dec, defaults=defaults)
            if created == True:
                print(f' Created unit: {data_object.repr}')
            else:
                print(f' Update unit: {data_object.repr}')
        print('')

@transaction.atomic
def filling_rates_vat():
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
            data_object, created = RateVAT.objects.update_or_create(code_str=code_str, defaults=defaults)
            if created == True:
                print(f' Created VAT rate: {data_object.repr}')
            else:
                print(f' Update VAT rate: {data_object.repr}')
        print('')

@transaction.atomic
def filling_cargo_hazard():
    print('Filling cargo hazards data:')
    path_file = f'{os.getcwd()}/classifiers/filling/cargo_hazard.json'
    with open(path_file, 'r') as file:
        json_data = json.load(file)
        for item_data in json_data:
            code_str = item_data.get('code_str', '')
            comment = item_data.get('_comment', '')
            if comment:
                continue
            defaults = {
                'name': item_data.get('name', '')
            }
            data_object, created = CargoHazard.objects.update_or_create(code_str=code_str, defaults=defaults)
            if created == True:
                print(f' Created cargo hazard: {data_object.repr}')
            else:
                print(f' Update cargo hazard: {data_object.repr}')
        print('')

def filling_all():
    filling_enum_unit_area_using()
    filling_enum_unit_type()
    filling_currency()
    filling_unit()
    filling_rates_vat()
    filling_cargo_hazard()