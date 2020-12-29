from django.db import models
from fountain.models.fountain import Fountain, FountainUpdateModel
from django.utils.translation import gettext_lazy as _
from users.models.user import User


class Update(models.Model):
    fountain_original = models.ForeignKey(Fountain,
                                          on_delete=models.CASCADE,
                                          verbose_name="Originial Fountain",
                                          related_name='fountian_updates')
    fountain_update = models.ForeignKey(FountainUpdateModel,
                                        on_delete=models.CASCADE,
                                        verbose_name="Modified Fountain",
                                        related_name='fountian_updates')

    user = models.ForeignKey(User, verbose_name=_(
        "User"), on_delete=models.CASCADE, related_name="update_fountians")