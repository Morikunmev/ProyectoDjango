from django.urls import path

from . import views
from django.conf import settings
from .views import VRegistro,cerrar_sesion,logear

urlpatterns = [
    path('',VRegistro.as_view(), name="Autentication"),
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),
    path('logear',logear,name="logear"),

]