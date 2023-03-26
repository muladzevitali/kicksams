from django.contrib import admin

from .models import (Country, CityName, City, Location)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(CityName)
class CityAdmin(admin.ModelAdmin):
    ...


@admin.register(City)
class CityLocationAdmin(admin.ModelAdmin):
    ...


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    ...
