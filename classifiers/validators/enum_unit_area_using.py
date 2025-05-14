
from django.core.exceptions import ValidationError
from classifiers.models import EnumUnitAreaUsing


def validate_enum_unit_area_using_code_str(value: str):
    if not EnumUnitAreaUsing.objects.filter(code_str=value).exists():
        raise ValidationError(f'There is no enumeration value for the unit area using ' + \
                              f'with the string code {value} in the database')
    return value
