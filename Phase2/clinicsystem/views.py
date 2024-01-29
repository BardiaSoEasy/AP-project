from django.shortcuts import render, redirect
from . import forms
from .import models
from django.contrib import messages
from .import system



def indexView(request):
    return render(request, 'index.html')

def loginView(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.filter(UserName=cd['UserName'], Password=cd['Password']).first()
            if user != None:
                if user.UserType == 'Patient':
                    return redirect('/clinicsystem/patient_panel')
                else:
                    return redirect('/clinicsystem/staff_panel/')
            else:
                messages.error(request, 'Invalid User', 'errormessage')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form':form})

def registerView(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.filter(UserName=cd['UserName'], Password=cd['Password']).first()
            if user == None:
                user = models.User.objects.create(UserName=cd['UserName'], Password=cd['Password'], Name=cd['Name'], EMail=cd['EMail'], UserType=cd['UserType'], IsLogin=True)
                return redirect('http://127.0.0.1:8000/')
            else:
                messages.error(request, 'User already exists', 'errormessage')
    else:
        form = forms.RegisterForm()
    return render(request, 'register.html', {'form':form})

def patientPanelView(request):
    return render(request, 'patient_panel.html')

def staffPanelView(request):
    return render(request, 'staff_panel.html')

def appointmentActiveListView(request):
  appointmentList = models.Appointment.objects.all().filter(Status='Booked')
  return render(request, 'appointment_active_list.html', {'appointmentList':appointmentList})

def appointmentHistoryListView(request):
  appointmentList = models.Appointment.objects.all().filter(Status='Cancelled')
  appointmentList = appointmentList | models.Appointment.objects.all().filter(Status__icontains='Paid')
  return render(request, 'appointment_history_list.html', {'appointmentList':appointmentList})

def updateprofileview(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.filter(UserName=cd['UserName']).first()
            if user is None:
                user = models.User.objects.create(UserName=cd['UserName'], Password=cd['Password'], Name=cd['Name'], EMail=cd['EMail'], UserType=cd['UserType'], IsLogin=True)
                messages.success(request, 'Profile updated successfully.')
                return redirect('http://127.0.0.1:8000/')
            else:
                messages.error(request, 'Username already taken', 'errormessage')
    else:
        form = forms.RegisterForm()
    return render(request, 'update_profile.html', {'form': form})


def appointmentreservationview(request):
    if request.method == 'POST':
        form = forms.AppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            clinic = models.Clinic.objects.get(ClinicId=cd['ClinicId'])
            service = models.Service.objects.get(ServiceId=cd['ServiceId'])
            datetime = cd['Date']
            if datetime == '':
                datetime = system.currentDateTime()
            status = cd['Status']
            time = cd['Time']
            # Create a new appointment
            new_appointment = models.Appointment.objects.create(
                ClinicId=clinic,  # pass the Clinic instance
                ServiceId=service,  # pass the Service instance
                UserName=request.user, 
                Date=datetime, 
                Time=time, 
                Status=status
            )
            messages.success(request, 'Appointment booked successfully.')
    else:
        form = forms.AppointmentForm()
    return render(request, 'appointment_reservation.html', {'form': form})




def viewCurrentAppointmentsstaff(request):
    appointment_list = models.Appointment.objects.all()
    return render(request, 'view_appointments.html', {'appointment_list': appointment_list})

def cancelAnAppointment(request):
    if request.method == 'POST':
        form = forms.CancelAppointmentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            appointment = models.Appointment.objects.get(AppointmentId=cd['AppointmentId'])
            if appointment:
                appointment.delete()
                messages.success(request, 'Appointment cancelled successfully.')
                return redirect('view_appointments')
    else:
        form = forms.CancelAppointmentForm()
    return render(request, 'cancel_appointment.html', {'form': form})


def increaseClinicAppointmentCounter(request):
    if request.method == 'POST':
        form = forms.IncreaseAppointmentCounterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            clinic = models.Clinic.objects.get(ClinicId=cd['ClinicId'])
            if clinic:
                clinic.AppointmentCounter += cd['Count']
                clinic.save()
                messages.success(request, 'Clinic appointment counter increased successfully.')
    else:
        form = forms.IncreaseAppointmentCounterForm()
    return render(request, 'increase_counter.html', {'form': form})
