from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

# Stranica za registrovanje korisnika
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successfull"))
            return redirect("home")
    else:
        form = RegisterUserForm()

    return render(
        request,
        "auth/register.html",
        {
            "form": form,
        },
    )


# Logovanje
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(
                request, ("Nastala je greška prilikom logovanja, pokušajte ponovo...")
            )
            return redirect("login")
    else:
        return render(request, "auth/login.html", {})


# Odjava


def logout_user(request):
    logout(request)
    messages.success(request, ("Uspešno ste odjavljeni"))
    return redirect("home")
