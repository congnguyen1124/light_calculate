from django.contrib import admin
from django.urls import path
from lights_calculate.views import calculate_light
from . import views

urlpatterns = [
    path('calculate-lights/', calculate_light, name='calculate_lights'),
]
