from django import forms
from .models import Flight, Cart

class FlightForm(forms.ModelForm):
    """Form for creating or updating flight details."""
    class Meta:
        model = Flight
        fields = [
            'flight_number',
            'departure_city',
            'arrival_city',
            'departure_time',
            'arrival_time',
            'price',
            'status'
        ]
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'flight_number': 'Flight Number',
            'departure_city': 'Departure City',
            'arrival_city': 'Arrival City',
            'departure_time': 'Departure Time',
            'arrival_time': 'Arrival Time',
            'price': 'Price (USD)',
            'status': 'Flight Status',
        }

class CartUpdateForm(forms.ModelForm):
    """Form for updating cart item details, such as the number of passengers."""
    class Meta:
        model = Cart  # Use CartItem instead of Cart to represent individual cart items
        fields = ['passengers']
        widgets = {
            'passengers': forms.NumberInput(attrs={
                'min': 1,
                'step': 1,
                'class': 'form-control',
            }),
        }
        labels = {
            'passengers': 'Number of Passengers',
        }
