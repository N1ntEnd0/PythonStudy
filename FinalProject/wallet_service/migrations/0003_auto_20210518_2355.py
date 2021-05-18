# Generated by Django 3.2.2 on 2021-05-18 20:55

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_service', '0002_auto_20210516_0100'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test1',
        ),
        migrations.AlterField(
            model_name='transactionlogs',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='transactionlogs',
            name='recipient',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionlogs',
            name='sender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
