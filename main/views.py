from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from main.models import Location
from .forms import LocationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "main/home.html")


def add_venue(request):
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
