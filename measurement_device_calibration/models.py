from django.db import models
from django.utils import timezone
# from .choices import *

class MeasurementDevice(models.Model):
    device_name = models.CharField(max_length = 50, verbose_name = 'שם פריט')
    manufacturer_id = models.CharField(max_length = 50, verbose_name = 'מספר יצרן')
    AF_id = models.CharField(max_length = 50, verbose_name = 'מסח"א')
    measurement_device_id = models.CharField(max_length = 16, verbose_name = "מס' סידורי של מכשיר הבדיקה")
    # test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    calibration_date = models.DateField(default = timezone.now, verbose_name = 'תאריך כיול אחרון')
    expiration_date = models.DateField(verbose_name = 'בתוקף עד')

    def __str__(self):
        return self.device_name
