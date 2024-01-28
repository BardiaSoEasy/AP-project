from django.db import models
from django.core.exceptions import ValidationError

from datetime import datetime





from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    usertype = models.CharField(max_length=1, choices=[('p', 'Patient'), ('s', 'Staff')])
    last_login = models.DateTimeField(null=True)

    @classmethod
    def register(cls, username, password, name, email, usertype):
        if cls.objects.filter(username=username).exists():
            return None  # Or raise an exception
        if usertype not in ['p', 's']:
            raise ValueError('Invalid user type')
        user = cls.objects.create(username=username, name=name, email=email, password=make_password(password), usertype=usertype)
        return user

    @classmethod
    def login(cls, username, password):
        try:
            user = cls.objects.get(username=username)
            if check_password(password, user.password):  # Check the password
                return user
        except cls.DoesNotExist:
            pass
        return None
    
    @classmethod
    def getUser(cls, username):
        try:
            return cls.objects.get(username=username)
        except cls.DoesNotExist:
            return None

    def updateProfile(self, password, name, email):
        self.password = make_password(password)  # Hash the new password
        self.name = name
        self.email = email
        self.save()

    @classmethod
    def removeUser(cls, username):
        cls.objects.filter(username=username).delete()

    @classmethod
    def isUserExists(cls, username):
        return cls.objects.filter(username=username).exists()

  
from django.db import models

class Clinic(models.Model):
    clinicid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    availability = models.BooleanField(default=False)

    @classmethod
    def addClinic(cls, name, address, contact):
        clinic = cls(name=name, address=address, contact=contact)
        clinic.save()
        return clinic

    def updateClinicInfo(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
        self.save()

    def setAvailability(self, availability):
        self.availability = availability
        self.save()

    @classmethod
    def getClinicById(cls, clinicId):
        try:
            return cls.objects.get(pk=clinicId)
        except cls.DoesNotExist:
            return None

    @classmethod
    def removeClinic(cls, clinicId):
        cls.objects.filter(pk=clinicId).delete()

    @classmethod
    def getClinics(cls):
        return cls.objects.all()

    @classmethod
    def isClinicExists(cls, clinicid):
        return cls.objects.filter(pk=clinicid).exists()

from django.db import models

class Appointment(models.Model):
    appointmentid = models.AutoField(primary_key=True)
    clinicid = models.IntegerField()
    serviceid = models.IntegerField()
    username = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=1)

    @classmethod
    def bookAppointment(cls, clinicid, serviceid, username, datetime):
        appointment = cls(clinicid=clinicid, serviceid=serviceid, username=username, datetime=datetime, status="B")
        appointment.save()
        return appointment

    @classmethod
    def clinicExists(cls, clinicId):
        return cls.objects.filter(clinicid=clinicId).exists()

    @classmethod
    def getCurrentAppointments(cls, username):
        return cls.objects.filter(username=username, status="B")

    @classmethod
    def getAppointmentsHistory(cls, username):
        return cls.objects.filter(username=username)

    @classmethod
    def getAppointments(cls):
        return cls.objects.all()

    @classmethod
    def cancelAnAppointment(cls, appointmentid, clinicid, username):
        try:
            appointment = cls.objects.get(appointmentid=appointmentid, clinicid=clinicid, username=username)
            appointment.status = "C"
            appointment.save()
        except cls.DoesNotExist:
            pass

    @classmethod
    def isAppointmentExists(cls, appointmentid):
        return cls.objects.filter(appointmentid=appointmentid).exists()


from django.db import models
from django.utils import timezone

class Notification(models.Model):
    notificationid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=timezone.now)
    message = models.TextField()

    @classmethod
    def sendMessage(cls, username, email, message):
        notification = cls(username=username, message=message)
        notification.save()
        # sendEmail(email=email, message=message)  

class Service(models.Model):
    serviceid = models.AutoField(primary_key=True)
    clinicid = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    @classmethod
    def addService(cls, clinicid, name, price):
        service = cls(clinicid=clinicid, name=name, price=price)
        service.save()
        return service

    def updateService(self, clinicid, name, price):
        self.clinicid = clinicid
        self.name = name
        self.price = price
        self.save()

    @classmethod
    def viewServices(cls, clinicid):
        return cls.objects.filter(clinicid=clinicid)

    @classmethod
    def getServiceById(cls, serviceid):
        try:
            return cls.objects.get(pk=serviceid)
        except cls.DoesNotExist:
            return None

    @classmethod
    def removeService(cls, serviceid):
        cls.objects.filter(pk=serviceid).delete()

    @classmethod
    def getClinicServices(cls, clinicid):
        return cls.objects.filter(clinicid=clinicid)

from django.db import models
from django.utils import timezone

class Payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    appointmentid = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()

    @classmethod
    # def addPayment(cls, appointmentid, serviceid):
        # datetime = timezone.now()
        
        # #amount = selectServicePrice(serviceid=serviceid)
        # payment = cls(appointmentid=appointmentid, datetime=datetime, #amount=amount)
        # payment.save()
        # return payment

    def updatePayment(self, appointmentid, datetime, amount):
        self.appointmentid = appointmentid
        self.datetime = datetime
        self.amount = amount
        self.save()

    @classmethod
    def viewPayments(cls, appointmentid):
        return cls.objects.filter(appointmentid=appointmentid)

