from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cars', views.cars, name='cars'),
    path('cars/<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search')
]