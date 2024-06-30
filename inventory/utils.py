from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

#validate unit value
def validate_unit(value):
    valid_units = ['kg', 'g', 'L', 'ml']
    parts = value.split()
    if len(parts) != 2:
        raise ValidationError("Unit must be in the format of a numeric value followed by a unit (e.g., '100 kg', '200 L').") 
    numeric_part, unit = parts
    try:
        numeric_part = float(numeric_part)
    except ValueError:
        raise ValidationError("The numeric part of the unit must be a number.")
    
    if unit not in valid_units:
        raise ValidationError(f"Unit must be one of the following: {",".join(valid_units)}")
    return unit 
    
# validating email
def validate_lowercase_email(email):
    email = email.lower()
    validator = EmailValidator()
    try:
        validator(email)
    except ValidationError as e:
        raise ValidationError(f"Invalid email: {e}")
    return email


# validating order date
def validate_order_date(expected_delivery_date, order_date):
    if order_date and order_date < expected_delivery_date:
        raise ValidationError("Order date cannot be before the expected delivery date.")
    return order_date
    