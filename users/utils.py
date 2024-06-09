import phonenumbers
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validate_phone_number(value):
    try:
        parsed_number = phonenumbers.parse(value,None)
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError('Invalid phone number')
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError('Invalid phone number')


def validate_lowercase_email(email):
    email = email.lower()
    validator = EmailValidator()
    try:
        validator(email)
    except ValidationError as e:
        raise ValidationError(f"Invalid email: {e}")
    return email