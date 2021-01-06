from django.urls import path, include
from fountain.urls import router as fountainRouter
from users.urls import router as userRouter

urlpatterns = [
    path('', include(fountainRouter.urls)),
    path('', include(userRouter.urls)),
]
