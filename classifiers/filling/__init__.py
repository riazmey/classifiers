"""
    Script to import data from .json files
    To execute this script run:
        1) python manage.py shell
        2) from classifiers.filling import filling_all
        3) filling_all()
        4) exit()
"""

from .filling import (
    filling_all,
    filling_enum_unit_area_using,
    filling_enum_unit_type,
    filling_currency,
    filling_unit,
    filling_rates_vat,
    filling_cargo_hazard,
    filling_legal_type)

__all__ = [
    filling_all,
    filling_enum_unit_area_using,
    filling_enum_unit_type,
    filling_currency,
    filling_unit,
    filling_rates_vat,
    filling_cargo_hazard,
    filling_legal_type
]
