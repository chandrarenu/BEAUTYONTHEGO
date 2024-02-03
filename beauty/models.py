from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Salon(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Stylist(models.Model):
    name = models.CharField(max_length=100)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
