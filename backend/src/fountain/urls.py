from fountain.api.fountain_views import FountainViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'fountain', FountainViewSet)
urlpatterns = router.urls
