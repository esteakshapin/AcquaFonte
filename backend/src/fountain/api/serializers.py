from rest_framework import serializers
from fountain.models.fountain import Fountain
from fountain.models.update import Update


class FountainSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Fountain
        fields = '__all__'

    def get_distance(self, obj):
        try:
            if obj.distance.mi >= 1:
                return str(round(obj.distance.mi, 2)) + ' miles'
            return str(round(obj.distance.ft, 5)) + ' feet'
        except AttributeError as error:
            return None


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = '__all__'
