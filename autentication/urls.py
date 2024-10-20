from django.urls import path

from . import views
from django.conf import settings
from .views import VRegistro

urlpatterns = [
    path('',VRegistro.as_view(), name="Autentication"),
]