import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validation_six_digits(value):
    if len(str(value)) != 6:
        raise ValidationError(
            _('%(value)s is not six digits'),
            params={'value':value}
        )


def validation_stock(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s% Not enough stock'),
            params={'value':value}
        )


def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


