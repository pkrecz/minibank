# Generated by Django 5.0.3 on 2024-09-08 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minibankapp', '0018_logmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logmodel',
            old_name='date_log',
            new_name='Date_log',
        ),
        migrations.RenameField(
            model_name='logmodel',
            old_name='id_log',
            new_name='Id_log',
        ),
    ]
