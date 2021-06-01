from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from .choices import *

class User(AbstractUser):
    full_name = models.CharField(default = '-', max_length = 50)
    personal_number = models.CharField(blank = True, max_length = 7, validators = [RegexValidator(regex = r'\d{7}')])
    level = models.IntegerField(default = 1, choices = LEVEL)


    def __str__(self):
        return str(self.full_name)

class Test(models.Model):
    # might be useful to change choices to foreign key so admins can add choices without changing the code
    department = models.IntegerField(choices = DEPARTMENT, verbose_name = 'מחלקה')
    test_date = models.DateField(verbose_name = 'תאריך ביצוע הבדיקה')
    test_time_start = models.TimeField(verbose_name = 'שעת תחילת הבדיקה')
    test_time_end = models.TimeField(verbose_name = 'שעת סיום הבדיקה')
    test_location = models.IntegerField(choices = LOCATION, verbose_name = 'מקום ביצוע הבדיקה')
    number_of_parts = models.IntegerField(default = 1, verbose_name = 'מספר פריטים בבדיקה')
    aircraft = models.CharField(max_length = 50, verbose_name = 'כלי טייס/מכלול')
    aircraft_id = models.CharField(max_length = 50, verbose_name = "מס' זנב/סידורי")
    meter_id = models.CharField(max_length = 16, blank = True, verbose_name = "מס' סידורי של מכשיר הבדיקה")

    # fields related to part
    part_description = models.CharField(max_length = 50, verbose_name = 'תיאור פריט')
    part_id = models.CharField(max_length = 16, blank = True, verbose_name = "מס' סידורי של הפריט")
    manufacturer_id = models.CharField(max_length = 16, blank = True, verbose_name = 'מספר יצרן')
    test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    literature_code = models.CharField(max_length = 50, verbose_name = 'שיוך לספרות טכנית')
    tag_number = models.CharField(max_length = 16 , blank = True, verbose_name = "מספר תג תהליך בדיקת אל הרס")
    testing_hours = models.FloatField(verbose_name = 'שעתון בדיקה')

    findings = models.IntegerField(choices = FINDINGS, blank = True, verbose_name = 'ממצאים')
    notes = models.CharField(max_length = 50, blank = True, verbose_name = 'הערות')

    tester = models.ForeignKey(
        User,
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
        return 'בדיקת ' + str(self.get_test_method_display()) + ' על ' + str(self.part_description)

class ReferanceItem(models.Model):
    part_description = models.CharField(max_length = 50, verbose_name = 'תיאור פריט')
    manufacturer_id = models.CharField(max_length = 50, verbose_name = 'מספר יצרן')
    test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    literature_code = models.CharField(max_length = 50, verbose_name = 'שיוך לספרות טכנית')
    testing_hours = models.FloatField(verbose_name = 'שעתון בדיקה')

    def __str__(self):
        return self.part_description

class TestItem(models.Model):
    part_description = models.CharField(max_length = 50, verbose_name = 'תיאור פריט')
    manufacturer_id = models.CharField(max_length = 50, verbose_name = 'מספר יצרן')
    test_method = models.IntegerField(choices = TEST_METHOD, verbose_name = 'שיטת בדיקה')
    literature_code = models.CharField(max_length = 50, verbose_name = 'שיוך לספרות טכנית')
    testing_hours = models.FloatField(verbose_name = 'שעתון בדיקה')

    def __str__(self):
        return self.part_description