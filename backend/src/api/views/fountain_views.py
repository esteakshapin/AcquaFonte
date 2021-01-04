from rest_framework.generics import ListAPIView, RetrieveAPIView
from fountain.models import Fountain
from fountain.api.serializers import FountainSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from fountain.api.fountain_filter_set import FountainFilter


class FountainDetailView(RetrieveAPIView):
    queryset = Fountain.objects.all()
    serializer_class = FountainSerializer


class FountainListView(ListAPIView):

    queryset = Fountain.objects.all()
    serializer_class = FountainSerializer
    filterset_class = FountainFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        longitude = self.request.query_params.get(
            'longitude', default='74.0060')
        latitude = self.request.query_params.get('latitude', default='40.7128')
        radius = self.request.query_params.get('radius', default=1)

        location = Point(float(longitude), float(latitude))

        queryset = queryset.filter(
            coords__distance_lte=(
                location,
                D(mi=radius)
            )
        ).annotate(distance=Distance('coords', location)).order_by('distance')

        return queryset
