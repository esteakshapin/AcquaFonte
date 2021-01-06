from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from fountain.models import Fountain

from users.managers import CustomUserManager

from dry_rest_permissions.generics import allow_staff_or_superuser, authenticated_users
from django.contrib.auth.models import Group


class User(AbstractUser):
    # custom user fields
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group, related_name='users_in_group', verbose_name='Groups')

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
        return self.email

    # read perms

    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_read_permission(request):
        print('global read permission')
        return True

    @authenticated_users
    def has_object_read_permission(self, request):
        print(request.user.has_perm('users.view_user'))
        return self == request.user \
            and request.user.has_perm('users.view_user')

    # write perms
    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_write_permission(request):
        return True

    @authenticated_users
    def has_object_write_permission(self, request):
        return self == request.user \
            and request.user.has_perm('users.change_user')

    # list perm
    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_list_permission(request):
        return False

    # create perm
    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_create_permission(request):
        return False
