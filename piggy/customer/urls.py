from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('customer_registration', customer_registration, name='customer_registration'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout')
]