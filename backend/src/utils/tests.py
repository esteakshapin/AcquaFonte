from users.models.user import User

from django.shortcuts import reverse

from urllib.parse import urlsplit


def set_super_user(user):
    user.is_staff = True
    user.is_superuser = True
    user.save()


def create_user_object(email, first_name, last_name):
    return User.objects.create_user(email=email,
                                    password='random_password',
                                    first_name=first_name,
                                    last_name=last_name)
