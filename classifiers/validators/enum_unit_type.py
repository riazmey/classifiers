
from django.core.exceptions import ValidationError
from classifiers.models import EnumUnitType


def validate_enum_unit_type_code_str(value: str):
    if not EnumUnitType.objects.filter(code_str=value).exists():
        raise ValidationError(f'There is no enumeration value for the unit type ' + \
                              f'with the string code {value} in the database')
    return value
