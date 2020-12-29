from rest_framework import serializers
from fountain.models.fountain import Fountain
from fountain.models.update import Update


class FountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fountain
        fields = '__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'
