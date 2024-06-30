from django.core.exceptions import ValidationError

def validate_end_date(start_date, end_date):
    if end_date <= start_date:
        raise ValidationError("end date must be after start date.")
    