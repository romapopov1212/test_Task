import django_filters

from .models import *

class CarFilter(django_filters.FilterSet):
    
    min_mileage = django_filters.NumberFilter(field_name="mileage", lookup_expr='gte')
    max_mileage = django_filters.NumberFilter(field_name="mileage", lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    id = django_filters.NumberFilter(field_name="id")
    
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['mileage', 'price']