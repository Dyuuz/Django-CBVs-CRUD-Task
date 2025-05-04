import datetime
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Car

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'ownership': _('Ownership'),
            'plate_number': _('Plate Number'),
            'driver': _('Driver'),
            'car_type': _('Car Type'),
            'insurance': _('Insurance'),
            'insurance_expiry_date': _('Insurance Expiry Date'),
            'status': _('Status'),
            'year': _('Year'),
            'car_serial_number': _('Car Serial Number'),
        }

        widgets = {
            'insurance_expiry_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select expiry date'}),
        }

    def clean_plate_number(self):
        plate = self.cleaned_data['plate_number']
        if Car.objects.filter(plate_number=plate).exists():
            raise forms.ValidationError(_('This plate number already exists.'))
        return plate

    def clean_car_serial_number(self):
        serial = self.cleaned_data['car_serial_number']
        if Car.objects.filter(car_serial_number=serial).exists():
            raise forms.ValidationError(_('This serial number already exists.'))
        return serial
    
    def clean_insurance_expiry_date(self):
        expiry_date = self.cleaned_data.get('insurance_expiry_date')
        if expiry_date and expiry_date < datetime.date.today():
            raise forms.ValidationError(_('The insurance expiry date cannot be in the past.'))
        return expiry_date

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'ownership': _('Ownership'),
            'plate_number': _('Plate Number'),
            'driver': _('Driver'),
            'car_type': _('Car Type'),
            'insurance': _('Insurance'),
            'insurance_expiry': _('Insurance Expiry Date'),
            'status': _('Status'),
            'year': _('Year'),
            'car_serial_number': _('Car Serial Number'),
        }

        widgets = {
            'insurance_expiry_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select expiry date'}),
        }

    def clean_plate_number(self):
        plate = self.cleaned_data.get('plate_number')
        if Car.objects.exclude(pk=self.instance.pk).filter(plate_number=plate).exists():
            raise forms.ValidationError(_('A car with this plate number already exists.'))
        return plate
    
    def clean_serial_number(self):
        sn = self.cleaned_data.get('car_serial_number')
        if Car.objects.exclude(pk=self.instance.pk).filter(car_serial_number=sn).exists():
            raise forms.ValidationError(_('A car with this serial number already exists.'))
        return sn
    
    def clean_insurance_expiry_date(self):
        expiry_date = self.cleaned_data.get('insurance_expiry_date')
        if expiry_date and expiry_date < datetime.date.today():
            raise forms.ValidationError(_('The insurance expiry date cannot be in the past.'))
        return expiry_date