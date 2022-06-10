from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Location(models.Model):
    ime = models.CharField("Ime Lokacije", max_length=200)
    adresa = models.CharField("Adresa", max_length=200)
    tel = models.CharField("Broj Telefona", max_length=15)
    web = models.URLField("Web Adresa", blank=True)
    email = models.EmailField("Email Adresa", blank=True)
    owner = models.IntegerField("Vlasnik Lokacije", blank=True, default=1)
    location_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.ime


class NightBirdUser(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    email = models.EmailField("Mail Korisnika")

    def __str__(self):
        return self.ime + " " + self.prezime


class Event(models.Model):
    ime = models.CharField("Naziv Dešavanja", max_length=120)
    event_date = models.DateTimeField("Datum Dogadjaja")
    location = models.ForeignKey(
        Location, blank=True, null=True, on_delete=models.CASCADE
    )
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    opis = models.TextField(blank=True)
    gosti = models.ManyToManyField(NightBirdUser, blank=True)

    def __str__(self):
        return self.ime
