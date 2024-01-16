class User:
    def __init__(self, user_id, name, email, password, user_type):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type
        self.logged_in = False

    def register(self):
        # Add your validation logic here
        pass

    def login(self, user_id, username, email, password, user_type):
        if username == self.name and password == self.password and user_id == self.user_id and email == self.email and user_type == self.user_type:
            self.logged_in = True
            print("Logged in successfully")
        else:
            print("Invalid username or password")

    def update_profile(self, new_email, new_password):
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


class Clinic:
    def __init__(self, clinic_id, name, address, contact_info, services, availability):
        self.clinic_id = clinic_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.services = services
        self.availability = availability

    def add_clinic(self, clinic_id, name, address, contact_info, services, availability):
        self.clinic_id = clinic_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.services = services
        self.availability = availability

    def update_clinic_info(self, name=None, address=None, contact_info=None, services=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if contact_info:
            self.contact_info = contact_info
        if services:
            self.services = services

    def set_availability(self, availability):
        self.availability = availability

    def view_appointment(self):
        pass


class Appointment:
    def __init__(self, appointment_id, clinic, user, date_time, status):
        self.appointment_id = appointment_id
        self.clinic = clinic
        self.user = user
        self.date_time = date_time
        self.status = status

    def register_appointment(self, new_datetime):
        current_time = datetime.now()
        if new_datetime < current_time:
            print("Cannot register an appointment in the past.")
            return
        self.date_time = new_datetime
        self.status = "Scheduled"
        print("Appointment registered successfully.")

    def cancel_appointment(self):
        self.status = "Cancelled"
        print("Appointment cancelled successfully.")

    def reschedule_appointment(self, new_datetime):
        self.register_appointment(new_datetime)
        print("Appointment rescheduled successfully.")
class Notification:
    def __init__(self, notification_id, user, message, date_time):
        self.notification_id = notification_id
        self.user = user
        self.message = message
        self.date_time = date_time

    def send_notification(self):
        print(f"Notification sent to user {self.user.user_id} with message: {self.message}")


class Payment:
    def __init__(self, payment_id, user, clinic, appointment, amount, date, status):
        self.payment_id = payment_id
        self.user = user
        self.clinic = clinic
        self.appointment = appointment
        self.amount = amount
        self.date = date
        self.status = status

    def make_payment(self, payment_id, user, clinic, appointment, amount, date, status):
        self.payment_id = payment_id
        self.user = user
        self.clinic = clinic
        self.appointment = appointment
        self.amount = amount
        self.date = date
        self.status = status

    def confirm_payment(self):
        self.status = "Completed"

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


class Service:
    def __init__(self, service_id, clinic, name, description, price):
        self.service_id = service_id
        self.clinic = clinic
        self.name = name
        self.description = description
        self.price = price

    def add_service(self, service_id, clinic, name, description, price):
        self.service_id = service_id
        self.clinic = clinic
        self.name = name
        self.description = description
        self.price = price

    def update_service_info(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price

    def view_service(self):
        return {
            "service_id": self.service_id,
            "clinic": self.clinic.name,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }
    