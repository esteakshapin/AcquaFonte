from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User
from users.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.utils.is_owner import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    # allowning only superusers to check user list
    def get_permissions(self):
        if self.action == 'list' or self.action == 'delete':
            return [IsAdminUser(), IsAuthenticated()]
        return super(UserViewSet, self).get_permissions()

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        print(request.body)


# {
#     "saved_fountains": [0]
# }
