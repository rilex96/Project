from django import forms
from django.forms import ModelForm
from .models import Location, Event

# Forma za popunjavanje lokacije
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ("ime", "adresa", "tel", "web", "email", "location_image")

        widgets = {
            "ime": forms.TextInput(
                attrs={"class": "loc__form", "placeholder": "Unesite Ime Lokacije"}
            ),
            "adresa": forms.TextInput(
                attrs={"class": "loc__form", "placeholder": "Unesite Adresu"}
            ),
            "tel": forms.TextInput(
                attrs={"class": "loc__form", "placeholder": "Unesite Broj Telefona"}
            ),
            "web": forms.URLInput(
                attrs={
                    "class": "loc__form",
                    "placeholder": "Unesite Web Adresu Vaseg Lokala",
                }
            ),
            "email": forms.EmailInput(
                attrs={"class": "loc__form", "placeholder": "Unesite Vašu Email Adresu"}
            ),
        }
