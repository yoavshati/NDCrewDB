from django.db import models

class MeasurementDevice(models.Model):
    measurement_device_id = models.CharField(max_length = 16, verbose_name = "מס' סידורי של מכשיר הבדיקה")
