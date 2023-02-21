from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


"""Choices for the service and time fields"""
SERVICE_CHOICES = (
    ('Oil Change', 'Oil Change'),
    ('Tire Rotation', 'Tire Rotation'),
    ('Brake Service', 'Brake Service'),
    ('Tune Up', 'Tune Up'),
    ('Other', 'Other'),
)


"""Choices for the time field"""
TIME_CHOICES = (
    ('8:00 AM', '8:00 AM'),
    ('8:30 AM', '8:30 AM'),
    ('9:00 AM', '9:00 AM'),
    ('9:30 AM', '9:30 AM'),
    ('10:00 AM', '10:00 AM'),
    ('10:30 AM', '10:30 AM'),
    ('11:00 AM', '11:00 AM'),
    ('11:30 AM', '11:30 AM'),
    ('12:00 PM', '12:00 PM'),
    ('12:30 PM', '12:30 PM'),
    ('1:00 PM', '1:00 PM'),
    ('1:30 PM', '1:30 PM'),
    ('2:00 PM', '2:00 PM'),
    ('2:30 PM', '2:30 PM'),
    ('3:00 PM', '3:00 PM'),
    ('3:30 PM', '3:30 PM'),
    ('4:00 PM', '4:00 PM'),
    ('4:30 PM', '4:30 PM'),
    ('5:00 PM', '5:00 PM'),
)

"""Appointment model"""
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=100, choices=TIME_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service
