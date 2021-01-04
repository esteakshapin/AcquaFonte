from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from fountain.models.fountain_abstract import FountainAbstract

# Create your models here.


class Fountain(FountainAbstract):
    last_updated = models.DateTimeField(
        verbose_name='Last Update', blank=True, null=True)

    def __str__(self):
        return (self.title + ", " + str(self.status))

    def save(self, *args, **kwargs):
        if not self.last_updated:
            pass
            last_updated = timezone.now()
        return super(Fountain, self).save(*args, **kwargs)


class FountainUpdateModel(FountainAbstract):
    def __str__(self):
        return ("(UPDATE MODEL) " + self.title + "," + str(self.id))
