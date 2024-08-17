from django.db import models

# Create your models here.


class Car(models.Model):
    marka = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    type_fuel = models.CharField(max_length=13)
    type_KPP = models.CharField(max_length=14)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.marka

