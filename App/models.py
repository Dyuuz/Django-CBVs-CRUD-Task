from django.db import models
from django.utils.translation import gettext_lazy as _

# Vendor Model
class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Driver Model
class Driver(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Car Model
class Car(models.Model):
    class CarType(models.TextChoices):
        SEDAN = 'SEDAN', _('Sedan')
        SUV = 'SUV', _('SUV')
        TRUCK = 'TRUCK', _('Truck')
        VAN = 'VAN', _('Van')

    ownership = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name=_('Vendor'))
    plate_number = models.CharField(max_length=20, unique=True, verbose_name=_('Plate Number'))
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, verbose_name=_('Driver'))
    car_type = models.CharField(max_length=10, choices=CarType.choices, verbose_name=_('Car Type'))
    insurance = models.CharField(max_length=100, verbose_name=_('Insurance'))
    insurance_expiry_date = models.DateField(verbose_name=_('Insurance Expiry Date'))
    status = models.BooleanField(default=True, verbose_name=_('Status'))
    year = models.PositiveIntegerField(verbose_name=_('Year'))
    car_serial_number = models.CharField(max_length=100, unique=True, verbose_name=_('Car Serial Number'))

    def __str__(self):
        return f"{self.plate_number} - {self.car_type}"
