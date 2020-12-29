from django.db import models

from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from fountain.models.fountain_abstract import FountainAbstract

# Create your models here.


class Fountain(FountainAbstract):
    last_updated = models.DateTimeField(
        verbose_name='Last Update', auto_now_add=True)

    def __str__(self):
        return (self.title + "," + str(self.id))


class FountainUpdateModel(FountainAbstract):
    def __str__(self):
        return ("(UPDATE MODEL) " + self.title + "," + str(self.id))
