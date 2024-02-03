from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('salons/', SalonList.as_view(), name='salon-list'),
    path('stylists/', StylistList.as_view(), name='stylist-list'),
    path('services/', ServiceList.as_view(), name='service-list'),
    path('appointments/', AppointmentList.as_view(), name='appointment-list'),
    path('user/register/', UserRegistration.as_view(), name='user-register'),
    path('user/login/', UserLogin.as_view(), name='user-login'),
    path('user/profile/', UserProfile.as_view(), name='user-profile'),
    
     # APIs for Appointment Cancellation, Update User Profile, and Logout User
    path('appointments/cancel/<int:pk>/', CancelAppointment.as_view(), name='cancel-appointment'),
    path('user/profile/update/', UpdateUserProfile.as_view(), name='update-user-profile'),
    path('logout/', LogoutUser.as_view(), name='logout-user'),
    
     # APIs for Adding and Viewing Reviews
    path('salon/<int:pk>/review/', AddReview.as_view(), name='add-review'),
    path('salon/<int:pk>/reviews/', ViewReviews.as_view(), name='view-reviews'),

]
