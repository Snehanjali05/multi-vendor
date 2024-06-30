# Generated by Django 5.0.6 on 2024-06-30 13:15

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('address_line1', models.CharField(max_length=64)),
                ('address_line2', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('postal_code', models.CharField(max_length=8)),
                ('country', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(max_length=32, unique=True)),
                ('issued_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('due_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('status', models.CharField(choices=[('unpaid', 'UNPAID'), ('paid', 'PAID'), ('overdue', 'OVERDUE')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-issued_date'],
            },
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment_method', models.CharField(choices=[('credit_card', 'CREDIT_CARD'), ('debit_card', 'DEBIT_CARD'), ('paypal', 'PAYPAL'), ('cash', 'CASH'), ('bank_transfer', 'BANK_TRANSFER')], max_length=16)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('transaction_date', models.DateField(auto_now_add=True, db_index=True)),
                ('transaction_id', models.CharField(db_index=True, max_length=32, unique=True)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED'), ('failed', 'FAILED'), ('refunded', 'REFUNDED')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-transaction_date'],
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('reason', models.TextField(blank=True, null=True)),
                ('refund_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('completed', 'COMPLETED'), ('failed', 'FAILED')], max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-refund_date'],
            },
        ),
    ]
