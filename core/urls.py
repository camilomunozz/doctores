from django.urls import path
from . import views
from .views import ReservaPabellonList

urlpatterns = [
    path('agendar-pabellon/', views.agendar_pabellon, name='agendar_pabellon'),
    path('api/reservas/', ReservaPabellonList.as_view(), name='reserva-list'),
]
