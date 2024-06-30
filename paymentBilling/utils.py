from django.core.exceptions import ValidationError

def validate_due_date(issued_date, due_date):
    if due_date <= issued_date:
        raise ValidationError("Due date cannot be earlier than issued date.")
    
def validate_refund_amount(refund_amount, transaction_amount):
    if refund_amount > transaction_amount:
        raise ValidationError("Refund amount cannot be greater than the transaction amount..")
    