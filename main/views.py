import numbers
import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from main.admin import LocationAdmin
from django.contrib.auth.models import User
from main.models import Location
from .forms import LocationForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    name = User.first_name
    return render(
        request,
        "main/home.html",
        {
            "name": name,
        },
    )


def add_location(request):
    submitted = False
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.owner = (
                request.user.id
            )  # User id is the id of current logged in user who submits the form.
            location.save()
            return HttpResponseRedirect("/add_location?submitted=True")
    else:
        form = LocationForm
        if "submitted" in request.GET:
            submitted = True

    form = LocationForm
    return render(
        request,
        "main/add_location.html",
        {
            "form": form,
            "submitted": submitted,
        },
    )


# Pokazuje jednu lokaciju
def show_location(request, location_id):
    location = Location.objects.get(pk=location_id)
    location_owner = User.objects.get(pk=location.owner)
    form = LocationForm(request.POST or None)

    return render(
        request,
        "main/show_location.html",
        {"location": location, "location_owner": location_owner, "form": form},
    )


# Lista Lokala koji su dostupni
def list_locations(request):
    location_list = Location.objects.all()

    # Podesavanje da se lokacije pokazuju po stranicama :D
    p = Paginator(Location.objects.all(), 3)
    page = request.GET.get("page")
    locations = p.get_page(page)
    nums = "a" * locations.paginator.num_pages
    return render(
        request,
        "main/lista_lokala.html",
        {"location_list": location_list, "locations": locations, "nums": nums},
    )
