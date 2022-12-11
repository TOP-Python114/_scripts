from django.urls import path

from random import randrange as rr

from .views import index

urlpatterns = [
    path('', index),
]
