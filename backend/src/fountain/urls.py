from django.urls import path, include

from api.views.update_views import UpdateDetailView, UpdateListView
from api.views.fountain_views import FountainDetailView, FountainListView

urlpatterns = [
    path('update', UpdateListView.as_view()),
    path('update/<pk>', UpdateDetailView.as_view()),
    path('<pk>', FountainDetailView.as_view()),
    path('', FountainListView.as_view())
]
