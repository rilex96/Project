from django.contrib import admin
from .models import Location
from .models import NightBirdUser
from .models import Event

# Register your models here.
admin.site.register(NightBirdUser)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("ime", "adresa", "tel")
    ordering = ("ime",)
    search_fields = (
        "ime",
        "adresa",
    )
