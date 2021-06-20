from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator
from django.utils import timezone
from .choices import *

# adds fields to default user
# lets admins track work hours
class User(AbstractUser):
    username = models.CharField(max_length = 8, unique = True, validators = [RegexValidator(regex = r's\d{7}')])
    password = models.CharField(max_length = 200, default = make_password('aA12345678'))
    first_name = models.CharField(max_length = 50, blank = False)

    department = models.IntegerField(choices = DEPARTMENT)

    PT_level = models.IntegerField(default = 2, choices = LEVEL)
    MT_level = models.IntegerField(default = 2, choices = LEVEL)
    EC_level = models.IntegerField(default = 2, choices = LEVEL)
    UT_level = models.IntegerField(default = 2, choices = LEVEL)
    RT_level = models.IntegerField(default = 2, choices = LEVEL)
    visual_level = models.IntegerField(default = 2, choices = LEVEL)
    tap_level = models.IntegerField(default = 2, choices = LEVEL)
    PAUT_level = models.IntegerField(default = 2, choices = LEVEL)
    LST_level = models.IntegerField(default = 2, choices = LEVEL)
    IRT_level = models.IntegerField(default = 2, choices = LEVEL)

    groups = models.ForeignKey(Group, default = 1, on_delete = models.PROTECT)

    def __str__(self):
        return self.get_full_name()

class Test(models.Model):
    department = models.IntegerField(choices = DEPARTMENT, verbose_name = 'שיוך ארגוני')
    test_location = models.IntegerField(choices = LOCATION, verbose_name = 'מקום הבדיקה')

    test_date = models.DateField(default = timezone.now , verbose_name = 'תאריך הבדיקה')
    test_time_start = models.TimeField(verbose_name = 'שעת התחלה')
    test_time_end = models.TimeField(verbose_name = 'שעת סיום')

    aircraft = models.CharField(max_length = 50, verbose_name = 'כלי טייס/מכלול')
    aircraft_id = models.CharField(max_length = 50, verbose_name = "מס' זנב/סידורי")
    measurement_device_id = models.CharField(blank = True, max_length = 16, verbose_name = "מס' סידורי של מכשיר הבדיקה")

    findings = models.IntegerField(choices = FINDINGS, verbose_name = 'ממצאים')
    notes = models.CharField(blank = True, max_length = 50, verbose_name = 'הערות')

    tester = models.ForeignKey(
        User,
        blank = True,
        null = True,
        on_delete = models.PROTECT,
        related_name = "tester",
        related_query_name = "tester",
        verbose_name = 'מבצע'
    )
    checker = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        related_name = "checker",
        related_query_name = "checker",
        verbose_name = 'בודק'
    )
    
    def __str__(self):
        return str(self.tester) + ', ' + str(self.test_date)

# saves item types for automatic field filling
class ReferenceItem(models.Model):
    part_description = models.CharField(max_length = 50, verbose_name = 'תיאור פריט')
    manufacturer_id = models.CharField(max_length = 50, verbose_name = 'מספר יצרן')
    test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    literature_code = models.CharField(max_length = 50, verbose_name = 'שיוך לספרות טכנית')
    testing_hours = models.FloatField(verbose_name = 'שעתון בדיקה')

    def __str__(self):
        return self.part_description

# allows user to save multiple items
# allows admins to modify specific items
class TestItem(models.Model):
    test = models.ForeignKey(Test, on_delete = models.CASCADE, related_name = 'items')

    part_description = models.CharField(max_length = 50, verbose_name = 'תיאור פריט')
    number_of_parts = models.IntegerField(verbose_name = 'מספר פריטים')
    item_id = models.CharField(blank = True, max_length = 50, verbose_name = 'מספר סידורי')
    tag_number = models.CharField(blank = True, max_length = 50, verbose_name = 'מספר תג תהליך')

    # automatically filled using js
    manufacturer_id = models.CharField(max_length = 50, verbose_name = 'מספר יצרן')
    test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    literature_code = models.CharField(max_length = 50, verbose_name = 'שיוך לספרות טכנית')
    testing_hours = models.FloatField(verbose_name = 'שעתון בדיקה')

    def __str__(self):
        return self.part_description