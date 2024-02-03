from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class SalonList(generics.ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
