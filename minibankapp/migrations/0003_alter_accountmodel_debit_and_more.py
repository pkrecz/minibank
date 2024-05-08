# Generated by Django 5.0.3 on 2024-04-21 10:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minibankapp', '0002_accountmodel_debit_accountmodel_free_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='Debit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Debet'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='Free_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Wolne środki'),
        ),
    ]
