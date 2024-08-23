# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError


def validator_free_balance(value):
    if value < 0:
        raise ValidationError('Value operation / Debit out of free balance limit.')
    return value

def validator_number_iban(value):
    if len(value) != 28:
        raise ValidationError('IBAN number should have 28 characters!')
    return value
