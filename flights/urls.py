from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_status, name='flight_status'),
    path('api/flight-status', views.api_flight_status, name='api_flight_status'),
]