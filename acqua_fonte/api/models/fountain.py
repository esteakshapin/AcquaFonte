from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Fountain(models.Model):
    # status of the fountian
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    UNKOWN = 'unknown'
    STATUS = [
        (ACTIVE, _("Active")),
        (INACTIVE, _("Not Working")),
        (UNKOWN, _("Unknown"))
    ]

    #features that the fountain has
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

    lat = models.DecimalField(max_digits=12, decimal_places=10, blank=False)
    lng = models.DecimalField(max_digits=13, decimal_places=10, blank=False)
    title = models.CharField(max_length=64, blank=False)
    status = models.CharField(max_length=10, choices=STATUS, default=UNKOWN)
    feature = models.IntegerField(choices=FEATURES, blank=True)
    access = models.CharField(max_length=10, choices=ACCESS, blank=False, defualt=PUBLIC)
    location = models.CharField(max_length=10, choices=LOCATION, blank=False, default=OUTDOOR)


    # implement type
    # type


