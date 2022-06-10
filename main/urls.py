from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_location", views.add_location, name="add_location"),
    path("show_location/<location_id>", views.show_location, name="show_location"),
    path("list_locations", views.list_locations, name="list_locations"),
]
