from django.db import models
from django.utils.translation import gettext
from model_utils.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = gettext('Country')
        verbose_name_plural = gettext('Countries')

    def __str__(self):
        return self.name


class CityName(TimeStampedModel):
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = gettext('City name')
        verbose_name_plural = gettext("City names")

    def __str__(self):
        return self.name


class City(TimeStampedModel):
    country = models.ForeignKey(to='locations.Country', on_delete=models.PROTECT, related_name='country_cities')
    city = models.ForeignKey(to='locations.CityName', on_delete=models.PROTECT, related_name='city_name_cities')

    class Meta:
        verbose_name = gettext('City')
        verbose_name_plural = gettext('Cities')
        db_table = 'city_locations'

    @property
    def name(self):
        return self.city.name

    def __str__(self):
        return f"{self.city.name} ({self.country.name})"


class Location(TimeStampedModel):
    city = models.ForeignKey(to='locations.City', on_delete=models.PROTECT, related_name='city_locations')

    class Meta:
        verbose_name = gettext('location')
        verbose_name_plural = gettext('locations')

    def __str__(self):
        return f'{self.city}'
