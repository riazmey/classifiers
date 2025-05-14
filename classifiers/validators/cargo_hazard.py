
from django.core.exceptions import ValidationError
from classifiers.models import CargoHazard


def validate_cargo_hazard_code_str(value: str):
    if not CargoHazard.objects.filter(code_str=value).exists():
        raise ValidationError(f'There are no entries in the classifier of dangerous goods ' + \
                              f'with the lowercase code {value} in the database')
    return value
