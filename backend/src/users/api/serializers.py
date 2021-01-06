from rest_framework import serializers
from users.models import User
from fountain.api.serializers import FountainSerializer, UpdateSerializer
from drf_braces.serializers.form_serializer import FormSerializer
from users.forms import CustomUserCreationForm
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer


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


class UserRegistrationFormSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate_username(self, username):
        pass

    def custom_signup(self, request, user):
        first_name = self.validated_data.get('first_name', '')
        last_name = self.validated_data.get('last_name', '')

        user.first_name = first_name
        user.last_name = last_name

        user.save()


class UserLogInSerializer(LoginSerializer):
    username = None
    email = serializers.EmailField(required=True, allow_blank=False)
