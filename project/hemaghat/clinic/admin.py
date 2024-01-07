from django.contrib import admin

from .models import User , Clinic, Appointment, Notification, Payment, Service

admin.site.register(User)
admin.site.register(Clinic)
admin.site.register(Appointment)
admin.site.register(Notification)
admin.site.register(Payment)
admin.site.register(Service)