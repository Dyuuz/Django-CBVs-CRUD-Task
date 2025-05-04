from django.contrib import admin
from .models import Car, Driver, Vendor

# Register your models here.
class CustomCar(admin.ModelAdmin):
    list_display = ('ownership','driver','plate_number','status',)  # Replace 'model_name' with an actual field from the Car model

class CustomDriver(admin.ModelAdmin):
    list_display = ('name',)

class CustomVendor(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Car, CustomCar)
admin.site.register(Driver, CustomDriver)
admin.site.register(Vendor, CustomVendor)