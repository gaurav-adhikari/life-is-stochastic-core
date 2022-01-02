from .views import welcome_api
from django.urls import path

urlpatterns = [
    path('', welcome_api),
]
