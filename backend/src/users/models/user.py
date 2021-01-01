from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from fountain.models import Fountain


class User(AbstractUser):
    avatar = models.ImageField(verbose_name=_('Avatar'),
                               help_text=_('Avatar of user'),
                               upload_to="Avatar",
                               blank=True)
    saved_fountains = models.ManyToManyField(Fountain,
                                             verbose_name=_("Saved Fountians"),
                                             related_name='users_saved')
    liked_fountains = models.ManyToManyField(Fountain,
                                             verbose_name=_(
                                                 "Liked Fountains"),
                                             related_name="users_liked")

    created_fountains = models.ManyToManyField(Fountain,
                                               verbose_name=_(
                                                   "Created Fountains"),
                                               related_name="user_created")
    updated_fountains = models.ManyToManyField(Fountain,
                                               verbose_name=_(
                                                   "Updated Fountains"),
                                               related_name="users_updated")

    def __str__(self):
        return self.username
