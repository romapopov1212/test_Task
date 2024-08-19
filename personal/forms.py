from django import forms
from django.forms import ModelForm
from .models import Car

class AddForm(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'type_fuel': forms.Select(),
            'type_KPP': forms.Select(),
        }