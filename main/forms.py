from django import forms
from django.forms.models import ModelForm, inlineformset_factory
from .models import *


# TEST
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        widgets = {
            'test_date': DateInput(),
            'test_time_start': TimeInput(),
            'test_time_end': TimeInput(),
        }
# TEST ITEM - inline
ItemFormSet = inlineformset_factory(Test, TestItem, exclude=[], extra=0, min_num=1)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'groups',
            'first_name',
            'last_name',
            'department',
            'PT_level',
            'MT_level',
            'EC_level',
            'UT_level',
            'RT_level',
            'visual_level',
            'tap_level',
            'PAUT_level',
            'LST_level',
            'IRT_level'
        ]

class PasswordForm(forms.Form):
    new_password = forms.CharField(min_length = 6, max_length = 20, label = 'סיסמה חדשה')

# REFERANCE ITEM
class ReferenceItemForm(forms.ModelForm):
    model = ReferenceItem
    fields = '__all__'