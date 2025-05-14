
from django.core.exceptions import ValidationError
from classifiers.models import RateVAT


def validate_rate_vat_code_str(value: str):
    if not RateVAT.objects.filter(code_str=value).exists():
        raise ValidationError(f'There are no entries in the classifier of rates vat ' + \
                              f'with the lowercase code {value} in the database')
    return value
