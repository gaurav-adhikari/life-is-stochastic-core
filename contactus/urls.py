from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactUsView,
)

router = DefaultRouter()
router.register("", ContactUsView)

urlpatterns = [
    path("", include(router.urls)),
]
