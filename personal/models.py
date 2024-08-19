from django.db import models

# Create your models here.


class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]
    
    KPP_CHOICES = [
        ('mechanical', 'Mechanical'),
        ('automatic', 'Automatic'),
        ('variator', 'Variator'),
        ('robot', 'Robot'),

    ]

    marka = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    type_fuel = models.CharField(max_length=13, choices=FUEL_CHOICES)
    type_KPP = models.CharField(max_length=14, choices=KPP_CHOICES)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.marka
