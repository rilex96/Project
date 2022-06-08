from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_location", views.add_venue, name="add_location"),
]
