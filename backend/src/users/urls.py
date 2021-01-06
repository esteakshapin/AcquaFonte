from users.api.user_views import UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)
urlpatterns = router.urls
