from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Salon
from .serializers import SalonSerializer
from rest_framework_simplejwt.views import TokenObtainPairView




class SalonList(generics.ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [AllowAny]
