from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

# class PersonnelForm(forms.ModelForm):
#     class Meta:
#         model = Personnel
#         fields = '__all__'

#     latest_course = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}), label='תאריך קורס אחרון')

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
        widgets = {
            'test_date': DateInput(),
            'test_time_start': TimeInput(),
            'test_time_end': TimeInput(),
        }
