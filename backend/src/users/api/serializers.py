from rest_framework import serializers
from users.models import User
from fountain.api.serializers import FountainSerializer, UpdateSerializer


class UserSerializer(serializers.ModelSerializer):
    saved_fountains = FountainSerializer(many=True)
    liked_fountains = FountainSerializer(many=True)
    created_fountains = UpdateSerializer(many=True)
    updated_fountains = UpdateSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'saved_fountains',
            'liked_fountains',
            'created_fountains',
            'updated_fountains',
        ]
