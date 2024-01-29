from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Clinic)
admin.site.register(models.Service)
admin.site.register(models.Appointment)
admin.site.register(models.Notification)
admin.site.register(models.Payment)
