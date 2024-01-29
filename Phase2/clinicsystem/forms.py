from django import forms
from .import models
class LoginForm(forms.Form):
    UserName=forms.CharField(required=True, label="User Name :")
    Password=forms.CharField(required=True, label="Password :", widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    UserName=forms.CharField(required=True, label="User Name :")
    Password=forms.CharField(required=True, label="Password :", widget=forms.PasswordInput())
    Name=forms.CharField(required=True, label='Name :')
    EMail=forms.CharField(required=True, label='EMail :')
    UserType=forms.ChoiceField(choices=[('Patient', 'Patient'), ('Staff', 'Staff')], label='User Type :')

class ClinicIdChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ClinicId

class ServiceIdChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.ServiceId

class AppointmentForm(forms.Form):
    AppointmentId = forms.IntegerField(required=False)
    ClinicId = ClinicIdChoiceField(queryset=models.Clinic.objects.all(), required=True, label="Clinic Id :")
    ServiceId = ServiceIdChoiceField(queryset=models.Service.objects.all(), required=True, label="Service Id :")
    Year = forms.ChoiceField(choices=[(year, year) for year in range(2024, 2100)], initial=2024, label="Year :")
    Month = forms.ChoiceField(choices=[(month, month) for month in range(1, 13)], initial=1, label="Month :")
    Day = forms.ChoiceField(choices=[(day, day) for day in range(1, 32)], initial=1, label="Day :")
    Time = forms.ChoiceField(choices=[('16:00','16:00'), ('16:30','16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00')], initial='16:00', label="Time :")
    Status = forms.ChoiceField(choices=[('Booked','Booked'), ('Cancelled','Cancelled'), ('Paid','Paid')], initial='Booked', label="Status :")
