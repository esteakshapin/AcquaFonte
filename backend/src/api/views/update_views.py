from rest_framework.generics import ListAPIView, RetrieveAPIView
from fountain.models.update import Update
from fountain.serializers import UpdateSerializer
# Create your views here.


class UpdateListView(ListAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer


class UpdateDetailView(RetrieveAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
