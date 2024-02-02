from django import forms
from . import models

class LoginForm(forms.Form):
    UserName=forms.CharField(required=True, label="User Name :")
    Password=forms.CharField(required=True, label="Password :", widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    UserName=forms.CharField(required=True, label="User Name :")
    Password=forms.CharField(required=True, label="Password :", widget=forms.PasswordInput())
    Name=forms.CharField(required=True, label='Name :')
    EMail=forms.CharField(required=True, label='EMail :')
    UserType=forms.ChoiceField(choices=[('Patient', 'Patient'), ('Staff', 'Staff')], label='User Type :')

class AppointmentForm(forms.ModelForm):
    AppointmentId = forms.IntegerField(disabled=True, label='Appointment Id :')
    Date = forms.CharField(label='Date :')
    Time = forms.ChoiceField(label='Time :', choices=[('16:00','16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00')])
    Status = forms.CharField(disabled=True, label='Status :')
    class Meta:
        model=models.Appointment
        fields=['AppointmentId', 'ClinicId', 'ServiceId', 'Date', 'Time', 'Status']

class ReserveForm(forms.ModelForm):
    Date = forms.CharField(label='Date :')
    Time = forms.ChoiceField(label='Time :', choices=[('16:00','16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00')])
    class Meta:
        model=models.Appointment
        fields=['ClinicId', 'ServiceId', 'Date', 'Time']

class ClinicForm(forms.ModelForm):
    Name=forms.CharField(required=True, label="Name :")
    Address=forms.CharField(required=True, label='Address :')
    Contact=forms.CharField(required=True, label='Contact :')
    class Meta:
        model=models.Clinic
        fields=['ClinicId', 'Name', 'Address', 'Contact']

class ServiceForm(forms.ModelForm):
    class Meta:
        model=models.Service
        fields=['ClinicId', 'Name', 'Price']

class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model=models.Payment
        fields=['AppointmentId']

class ClinicForm(forms.ModelForm):
    ClinicId = forms.IntegerField(disabled=True, label='Clinic Id :')
    Name = forms.CharField(label='Name :')
    Address = forms.CharField(label='Address :')
    Contact = forms.CharField(label='Contact :')
    Availability = forms.BooleanField(label='Availability :')
    class Meta:
        model=models.Appointment
        fields=['ClinicId', 'Name', 'Address', 'Contact', 'Availability']

class ServiceForm(forms.ModelForm):
    ServiceId = forms.IntegerField(disabled=True, label='Service Id :')
    Name = forms.CharField(label='Name :')
    Price = forms.IntegerField(label='Address :')
    class Meta:
        model=models.Appointment
        fields=['ServiceId', 'ClinicId', 'Name', 'Price']

class PaymentForm(forms.ModelForm):
    PaymentId = forms.IntegerField(disabled=True, label='Payment Id :')
    Amount = forms.IntegerField(label='Amount :')
    class Meta:
        model=models.Payment
        fields=['PaymentId', 'AppointmentId', 'Amount']
