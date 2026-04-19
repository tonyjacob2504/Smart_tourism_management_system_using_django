from django import forms
from .models import Package, Accommodation, Destination

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['place', 'person', 'days', 'price', 'guide', 'coordinator']

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['name', 'image', 'type', 'phone_number', 'email', 'address', 'total_rooms', 'checkin', 'checkout', 'price_per_night', 'room_type', 'password']
        widgets = {
            'checkin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'checkout': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'total_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control form-select'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Set a management password'}),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'image', 'state', 'city', 'best_season', 'entry_fees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'best_season': forms.TextInput(attrs={'class': 'form-control'}),
            'entry_fees': forms.NumberInput(attrs={'class': 'form-control'}),
        }
