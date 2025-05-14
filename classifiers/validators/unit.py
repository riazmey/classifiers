
from django.core.exceptions import ValidationError
from classifiers.models import Unit


def validate_unit_code_dec(value: str) -> str:
    if not Unit.objects.filter(code_dec=value).exists():
        raise ValidationError(f'There are no entries in the classifier of units of measurement ' + \
                              f'with the numeric code {value} in the database')
    return value

def validate_unit_notation_national(value: str) -> str:
    if not Unit.objects.filter(notation_national=value).exists():
        raise ValidationError(f'There are no entries in the classifier of units of measurement ' + \
                              f'with the symbol (national) {value} in the database')
    return value

def validate_unit_notation_international(value: str) -> str:
    if not Unit.objects.filter(notation_international=value).exists():
        raise ValidationError(f'There are no entries in the classifier of units of measurement ' + \
                              f'with the symbol (international) {value} in the database')
    return value
