from django_filters import rest_framework as filters
from fountain.models.fountain import Fountain
from api.utils.list_filter import ListFilter


class FountainFilter(filters.FilterSet):
    status = ListFilter(field_name='status')
    access = ListFilter(field_name='access')
    location = ListFilter(field_name='location')
    feature = ListFilter(field_name='feature')
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')

    class Meta:
        model = Fountain
        fields = ['status', 'feature', 'access',
                  'location', 'min_rating', 'max_rating']
