# Generated by Django 3.2.3 on 2021-06-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement_device_calibration', '0002_remove_measurementdevice_device_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurementdevice',
            name='device_name',
            field=models.CharField(default='md', max_length=50, verbose_name='שם פריט'),
            preserve_default=False,
        ),
    ]