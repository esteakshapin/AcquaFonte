from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .models import Fountian


class User(AbstractUser):
    avatar = models.ImageField(verbose_name=_('Avatar'),
                               help_text=_('Avatar of user'),
                               upload_to="Avatar",
                               blank=True)
    saved_fountains = models.ManyToManyField(Fountian,
                                             verbose_name=_("Saved Fountians"),
                                             related_name='users_saved')
    liked_fountains = models.models.ManyToManyField(Fountian,
                                                    verbose_name=_(
                                                        "Liked Fountains"),
                                                    related_nmae="users_liked")
