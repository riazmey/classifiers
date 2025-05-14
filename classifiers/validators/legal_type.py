
from django.core.exceptions import ValidationError
from classifiers.models import LegalType


def validate_legal_type_code_str(value: str):
    if not LegalType.objects.filter(code_str=value).exists():
        raise ValidationError(f'There are no entries in the classifier of organizational and legal forms ' + \
                              f'with the lowercase code {value} in the database')
    return value
