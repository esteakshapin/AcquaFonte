from django.db import models

from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.


class FountainAbstract(models.Model):
    # status of the fountian
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    UNKOWN = 'unknown'
    STATUS = [
        (ACTIVE, _("Active")),
        (INACTIVE, _("Not Working")),
        (UNKOWN, _("Unknown"))
    ]

    # features that the fountain has
    FEATURES = [
        (0, _("Bottle Refiller")),
        (1, _("Kid Friendly")),
        (2, _("Accesible")),
        (3, _("Pet Fiendly")),
    ]

    # fountain access
    PUBLIC = "Public"
    PRIVATE = 'Private'

    ACCESS = [
        (PUBLIC, _(PUBLIC)),
        (PRIVATE, _(PRIVATE))
    ]

    # location of the fountain
    INDOOR = "Indoor"
    OUTDOOR = "Outdoor"
    LOCATION = [
        (INDOOR, _(INDOOR)),
        (OUTDOOR, _(OUTDOOR))
    ]

    lat = models.DecimalField(
        max_digits=12, decimal_places=10, blank=False, null=False, default=0.0)

    lng = models.DecimalField(
        max_digits=13, decimal_places=10, blank=False, null=False, default=0.0)

    title = models.CharField(max_length=120, blank=False)

    status = models.CharField(max_length=10, choices=STATUS, default=UNKOWN)

    feature = MultiSelectField(choices=FEATURES, blank=True, null=True)

    access = models.CharField(
        max_length=10, choices=ACCESS, blank=False, default=PUBLIC)

    location = models.CharField(
        max_length=10, choices=LOCATION, blank=False, default=OUTDOOR)

    # # implement type
    # # type

    def __str__(self):
        return (self.title + "," + str(self.id))

    class Meta:
        abstract = True
