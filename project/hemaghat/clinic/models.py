from django.db import models
from django.core.exceptions import ValidationError
from .validators import username_validation , email_validation , password_validation
from datetime import datetime

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('Secretary', 'Secretary'),
    ]
    user_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200, validators=[username_validation])
    email = models.EmailField(max_length=200, validators=[email_validation])
    password = models.CharField(max_length=200, validators=[password_validation])
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    logged_in = models.BooleanField(default=False)

    def register(self):
        try:
            self.full_clean()  
        except ValidationError as e:
            print(e)

    def login(self, user_id , username, email, password, user_type):
        if username == self.name and password == self.password and user_id == self.user_id and email == self.email and user_type == self.user_type :
            self.logged_in = True
            print("Logged in successfully")
        else:
            print("Invalid username or password")
    
    def update_profile(self , new_email , new_password):
        if self.logged_in:
            self.email = new_email
            self.password = new_password
            print("Profile updated successfully")
        else:
            print("You need to log in first")
    
    def view_appointments(self):
        if self.logged_in:
            if self.user_type == "Doctor" or self.user_type == "Secretary":
                print("Appointments: ")
            else:
                print("You do not have permission to view appointments")
        else:
            print("You need to log in first")

class Clinic(models.Model):
    clinic_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    services = models.TextField()
    availability = models.BooleanField(default=True)

    def add_clinic(self, clinic_id, name, address, contact_info, services, availability):
        self.clinic_id = clinic_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.services = services
        self.availability = availability
        self.save()

    def update_clinic_info(self, name=None, address=None, contact_info=None, services=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if contact_info:
            self.contact_info = contact_info
        if services:
            self.services = services
        self.save()

    def set_availability(self, availability):
        self.availability = availability
        self.save()

    def view_appointment(self):
        pass

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]
    appointment_id = models.CharField(max_length=200)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    date_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def register_appointment(self, new_datetime):
        current_time = datetime.now()
        if new_datetime < current_time:
            print("Cannot register an appointment in the past.")
            return
        self.date_time = new_datetime
        self.status = "Scheduled"
        print("Appointment registered successfully.")
        self.save()

    def cancel_appointment(self):
        self.status = "Cancelled"
        print("Appointment cancelled successfully.")
        self.save()

    def reschedule_appointment(self, new_datetime):
        self.register_appointment(new_datetime)
        print("Appointment rescheduled successfully.")
        self.save()

class Notification(models.Model):
    notification_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_time = models.DateTimeField()

    def send_notification(self):
        print(f"Notification sent to user {self.user.user_id} with message: {self.message}")




class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]
    payment_id = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def make_payment(self, payment_id, user, clinic, appointment, amount, date, status):
        self.payment_id = payment_id
        self.user = user
        self.clinic = clinic
        self.appointment = appointment
        self.amount = amount
        self.date = date
        self.status = status
        self.save()

    def confirm_payment(self):
        self.status = "Completed"
        self.save()

    def view_payment(self):
        return {
            "payment_id": self.payment_id,
            "user": self.user.user_id,
            "clinic": self.clinic.clinic_id,
            "appointment": self.appointment.appointment_id,
            "amount": self.amount,
            "date": self.date,
            "status": self.status,
        }



class Service(models.Model):
    service_id = models.CharField(max_length=200)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def add_service(self, service_id, clinic, name, description, price):
        self.service_id = service_id
        self.clinic = clinic
        self.name = name
        self.description = description
        self.price = price
        self.save()

    def update_service_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        self.save()

    def view_service(self):
        return {
            "service_id": self.service_id,
            "clinic": self.clinic.name,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }