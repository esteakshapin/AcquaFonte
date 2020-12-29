from django.urls import path
from api.views.update_views import UpdateDetailView, UpdateListView

urlpatterns = [
    path('update', UpdateListView.as_view()),
    path('update/<pk>', UpdateDetailView.as_view())
]
