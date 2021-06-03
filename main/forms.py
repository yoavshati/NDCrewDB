from django import forms
from django.forms.models import inlineformset_factory
from .models import *

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

ItemFormSet = inlineformset_factory(Test, TestItem, exclude=[])