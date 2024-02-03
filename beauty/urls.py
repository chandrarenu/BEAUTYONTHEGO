from django.urls import path
from .views import *

urlpatterns = [
    path('salons/',SalonList.as_view(),name='salon-list'),
]
