# Generated by Django 3.2.3 on 2021-06-10 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210610_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='meter_id',
            new_name='measurement_device_id',
        ),
    ]
