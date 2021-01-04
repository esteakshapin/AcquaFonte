from django.urls import path, include

urlpatterns = [
    path('fountain', include('fountain.urls')),
    path('users/', include('users.urls')),
]
