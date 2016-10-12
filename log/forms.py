from django import forms
from django.forms import ModelForm

from .models import Log


class DateInput(forms.DateInput):
    input_type = 'date'

class LogForm(ModelForm):

    class Meta:
        model = Log
        fields = ['mesaid', 'barcode', 'wake']
        widgets = {
            'wake': DateInput(),
        }