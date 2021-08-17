from django.forms import ModelForm
from django.forms import ModelForm, TextInput, TextInput, EmailField
from django import forms
from .models import ReservationsRestaurant


class ReservationsRestaurantForm(forms.ModelForm):
    class Meta:
        model = ReservationsRestaurant
        fields = ['nom', 'numeroTel', 'mail', 'nombreDePersonnes', 'tables', 'date']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'numeroTel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero téléphone'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse email'}),
            'nombreDePersonnes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de personnes'}),
            'tables': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de table'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'Date'}),
        }