from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Car(models.Model):
    FUEL_CHOICES = [
        ('бензин', 'Бензин'),
        ('дизель', 'Дизель'),
        ('электричество', 'Электричество'),
        ('гибрид', 'Гибрид'),
    ]
    
    KPP_CHOICES = [
        ('механическая', 'Механическая'),
        ('автоматическая', 'Автоматическая'),
        ('вариатор', 'Вариатор'),
        ('робот', 'Робот'),

    ]

    marka = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    year = models.IntegerField()
    type_fuel = models.CharField(max_length=13, choices=FUEL_CHOICES)
    type_KPP = models.CharField(max_length=14, choices=KPP_CHOICES)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def clean(self):
        if self.year > 2024 or self.year <1900:
            raise ValidationError({'year': 'Год должен находить в промежутке от 1900 до 2024'})

    def checkMarka(self):
        if not(self.marka.isalpha()):
            raise ValidationError({'marka' : 'Марка машины может содержать только буквы'})

    def checkMileage(self):
        if self.mileage < 0:
            raise ValidationError({'mileage' : 'Пробег не может быть отрицательным'})

    def checkPrice(self):
        if self.price < 0:
            raise ValidationError({'price' : 'Цена не может быть отрицательной'})    

    def save(self, *args, **kwargs):
        self.clean()
        self.checkMarka()
        self.checkMileage()
        self.checkPrice()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.marka
