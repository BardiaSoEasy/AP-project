from django.contrib import admin
from . import models 
from .models import User , Clinic, Appointment, Notification, Payment, Service



admin.site.register([User, Clinic, Appointment , Notification ,Payment,  Service])