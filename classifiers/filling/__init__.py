"""
    Script to import data from .json files
    To execute this script run:
        1) python manage.py shell
        2) from classifiers.filling import filling_all
        3) filling_all()
        4) exit()
"""

from .filling import filling_all
from .filling import filling_currency
from .filling import filling_unit
from .filling import filling_rates_vat
from .filling import filling_cargo_hazard

__all__ = [
    filling_all,
    filling_currency,
    filling_unit,
    filling_rates_vat,
    filling_cargo_hazard,
]
