from django.core.exceptions import ValidationError

def validate_capacity(value):
    valid_units = ['kg', 'g', 'L', 'ml']
    parts = value.split()
    if len(parts) != 2:
        raise ValidationError("Capacity must be in the format of a numeric value followed by a unit (e.g., '100 kg', '200 L').") 
    
    numeric_part, unit = parts
    try:
        numeric_part = float(numeric_part)
    except ValueError:
        raise ValidationError("The numeric part of the capacity must be a number.")
    
    if unit not in valid_units:
        raise ValidationError(f"Unit must be one of the following: {",".join(valid_units)}")
    return unit 
    
    
def validate_delivery_times(expected_delivery_time, actual_delivery_time):
    if actual_delivery_time and actual_delivery_time < expected_delivery_time:
        raise ValidationError("Actual delivery time cannot be before the expected delivery time.")
    return actual_delivery_time
    