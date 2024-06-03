from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('customer_registration', customer_registration, name='customer_registration'),
]
