# Generated by Django 5.0.6 on 2024-06-30 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0002_initial'),
        ('paymentBilling', '0001_initial'),
        ('subscription', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.customerprofile'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order'),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.customerprofile'),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order'),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='subscription_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscription.subscription'),
        ),
        migrations.AddField(
            model_name='refund',
            name='payment_transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='paymentBilling.paymenttransaction'),
        ),
    ]
