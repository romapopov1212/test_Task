from django.forms import ModelForm

from .models import Car

class AddForm(ModelForm):
    class Meta:
        model = Car
        fields = ["marka", "model", "year", "type_fuel", "type_KPP", "mileage", "price"]
        