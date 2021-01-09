from rest_framework.generics import ListAPIView, RetrieveAPIView
from fountain.models import Fountain
from fountain.api.serializers import FountainSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from fountain.api.fountain_filter_set import FountainFilter
from rest_framework import viewsets
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.response import Response


class FountainViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    serializer_class = FountainSerializer
    queryset = Fountain.objects.all()
    permission_classes = (DRYPermissions,)

    def list(self, request):

        longitude = self.request.query_params.get(
            'longitude', default='-122.3321')
        latitude = self.request.query_params.get('latitude', default='47.6062')
        radius = self.request.query_params.get('radius', default=1)
        location = Point(float(longitude), float(latitude))

        queryset = Fountain.objects.filter(
            coords__distance_lte=(
                location,
                D(mi=radius)
            )
        ).annotate(distance=Distance('coords', location)).order_by('distance')

        serializer = FountainSerializer(queryset, many=True)
        return Response(serializer.data)
