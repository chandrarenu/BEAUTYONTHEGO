# beautyonthego_app/views.py
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Salon, Stylist, Service, Appointment
from .serializers import SalonSerializer, StylistSerializer, ServiceSerializer, AppointmentSerializer, UserSerializer

# Views for Salon, Stylist, Service, and Appointment
class SalonList(generics.ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class StylistList(generics.ListCreateAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Views for User Registration, User Login, and User Profile
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLogin(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserProfile(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Views for Appointment Cancellation, Update User Profile, and Logout User
class CancelAppointment(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class UpdateUserProfile(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Views for Adding and Viewing Reviews
class AddReview(generics.CreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class ViewReviews(generics.ListAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
