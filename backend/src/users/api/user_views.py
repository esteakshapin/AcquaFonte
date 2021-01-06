from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserSerializer
from dry_rest_permissions.generics import DRYPermissions


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (DRYPermissions,)


# {
#     "saved_fountains": [0]
# }
