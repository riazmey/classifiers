
from django.core.exceptions import ValidationError
from classifiers.models import Currency


def validate_currency_code_dec(value: str) -> str:
    if not Currency.objects.filter(code_dec=value).exists():
        raise ValidationError(f'There are no entries in the classifier of currency ' + \
                              f'with the numeric code {value} in the database')
    return value

def validate_currency_code_str(value: str):
    if not Currency.objects.filter(code_str=value).exists():
        raise ValidationError(f'There are no entries in the classifier of currency ' + \
                              f'with the lowercase code {value} in the database')
    return value
