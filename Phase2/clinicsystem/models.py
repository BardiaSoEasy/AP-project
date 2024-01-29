from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timezone
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    UserName = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    Name = models.CharField(max_length=50, null=False, blank=False)
    EMail = models.EmailField(max_length=255, null=False, blank=False)
    Password = models.CharField(max_length=50, null=False, blank=False)
    UserType = models.CharField(max_length=10, choices=[('Patient', 'Patient'), ('Staff', 'Staff')], default='Patient')
    IsLogin = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.Name
    
class Clinic(models.Model):
    ClinicId = models.AutoField(primary_key=True, null=False, blank=False)
    Name = models.CharField(max_length=50, null=False, blank=False)
    Address = models.CharField(max_length=255, null=False, blank=False)
    Contact = models.CharField(max_length=50, null=False, blank=False)
    Availability = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.Name

class Service(models.Model):
    ServiceId = models.AutoField(primary_key=True, null=False, blank=False)
    ClinicId = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=False, blank=False)
    Price = models.PositiveIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.Name

class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True, null=False, blank=False)
    ClinicId = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    ServiceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(null=False, blank=False)
    Time = models.CharField(max_length=10, choices=[('16:00','16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00')], default='16:00')
    Status = models.CharField(max_length=10, choices=[('Booked','Booked'), ('Cancelled','Cancelled'), ('Paid','Paid')], default='Booked')

    def __str__(self):
        return f"{self.ClinicId} / {self.ServiceId} / { self.UserName}"
    
class Notification(models.Model):
    NotificationId = models.AutoField(primary_key=True, null=False, blank=False)
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    DateTime = models.DateTimeField(null=False, blank=False)
    Message = models.TextField(null=False, blank=False)


class Payment(models.Model):
    PaymentId = models.AutoField(primary_key=True, null=False, blank=False)
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    DateTime = models.DateTimeField(auto_now=True, null=False, blank=False)
    Amount = models.PositiveIntegerField(default=0, null=False, blank=False)
