from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('master_registration', master_registration, name='master_registration'),
]
