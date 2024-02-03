from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import *


# for user registration and login
class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'