from django.db import models
from django.utils.translation import gettext
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(max_length=512, null=False, blank=False, verbose_name=gettext('name'))
    locations = models.ManyToManyField(to='locations.Location', related_name='location_companies',
                                       verbose_name=gettext('locations'))
    foundation_year = models.CharField(max_length=8, null=True, verbose_name=gettext('foundation year'))
    team_size = models.PositiveIntegerField(null=True, verbose_name=gettext('team size'))
    website = models.URLField(verbose_name=gettext('website'))
    description = models.TextField(verbose_name=gettext('description'))

    class Meta:
        verbose_name = gettext('Company')
        verbose_name_plural = gettext('Companies')

    def __str__(self):
        return f"{self.name}"
