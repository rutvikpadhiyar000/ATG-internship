from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor')

    req_speciality = models.CharField(max_length=15)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
