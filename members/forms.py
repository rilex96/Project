from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Registraciona Forma


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="Email Adresa")
    ime = forms.CharField(max_length=50)
    prezime = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "ime", "prezime", "email", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super(RegisterUserForm, self).__init__(*args, **kwargs)
            # Trebace mi pomoc oko menjanja labela za ove forme

            self.fields["username"].label = "Korisnicko Ime"
            self.fields["password1"].label = "Šifra"
            self.fields["password2"].label = "Ponovite Šifru"
