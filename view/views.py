from django.shortcuts import render, redirect
from . import forms
from .import models
from django.contrib import messages
from datetime import datetime

def indexView(request):
    request.session['currentUserName'] = ""
    request.session['currentUserType'] = ""
    return render(request, 'index.html')

def loginView(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.filter(UserName=cd['UserName'], Password=cd['Password']).first()
            if user != None:
                request.session['currentUserName'] = user.UserName
                request.session['currentUserType'] = user.UserType
                if user.UserType == 'Patient':
                    return redirect('/clinicsystem/patient_panel/')
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
                user = models.User.objects.create(UserName=cd['UserName'], Password=cd['Password'], Name=cd['Name'], EMail=cd['EMail'], UserType=cd['UserType'], IsLogin=False)
                return redirect('/')
            else:
                messages.error(request, 'User already exists', 'errormessage')
    else:
        form = forms.RegisterForm()
    return render(request, 'register.html', {'form':form})

def patientPanelView(request):
    return render(request, 'patient_panel.html', {'userName':request.session['currentUserName']})

def staffPanelView(request):
    return render(request, 'staff_panel.html', {'userName':request.session['currentUserName']})

def appointmentActiveListView(request):
  appointmentList = models.Appointment.objects.all().filter(Status='Booked')
  appointmentList = appointmentList & models.Appointment.objects.all().filter(UserName=request.session['currentUserName'])
  return render(request, 'appointment_active_list.html', {'appointmentList':appointmentList})

def appointmentHistoryListView(request):
  appointmentList = models.Appointment.objects.all().filter(UserName=request.session['currentUserName'])
  appointmentList = appointmentList & (models.Appointment.objects.all().filter(Status='Cancelled') | models.Appointment.objects.all().filter(Status__icontains='Paid'))
  return render(request, 'appointment_history_list.html', {'appointmentList':appointmentList})

def appointmentView(request, appointmentId):
    if request.session['currentUserName'] != "":
        appointment = models.Appointment.objects.filter(AppointmentId=appointmentId).first()
        print(request.method)
        if request.method == 'POST':
            form = forms.AppointmentForm(request.POST, instance=appointment)
            if form.is_valid():
                cd = form.cleaned_data
                if appointment != None:
                    appointment.AppointmentId = cd['AppointmentId']
                    appointment.ClinicId = cd['ClinicId']
                    appointment.ServiceId = cd['ServiceId']
                    appointment.Date = cd['Date']
                    appointment.Time = cd['Time']
                    appointment.save()
                    messages.info(request, 'Appointment updated successfully')
                    if request.session['currentUserType'] == 'Patient':
                        return redirect('/clinicsystem/patient_panel/')
                    else:
                        return redirect('/clinicsystem/staff_panel/')
                else:
                    messages.error(request, 'Appointment Id not found', 'errormessage')
            else:
                messages.error(request, 'ERROR')
        else:
            form = forms.AppointmentForm(instance=appointment)
    return render(request, 'appointment.html', {'form':form, 'appointmentId':appointmentId})

def cancelAppointmentView(request, appointmentId):
    if request.session['currentUserName'] != "":
        appointment = models.Appointment.objects.filter(AppointmentId=appointmentId, Status='Booked').first()
        if appointment != None:
            appointment.Status = 'Cancelled'
            appointment.save()
            messages.info(request, 'Appointment cancelled successfully')
            return redirect('/clinicsystem/patient_panel/')
        else:
            messages.error(request, 'Invalid Status For Cancelling', 'errormessage')            
    return render(request, 'appointment.html')

def clinicListView(request):
  clinicList = models.Clinic.objects.all()
  return render(request, 'clinic_list.html', {'clinicList':clinicList})

def paymentListView(request):
  paymentList = models.Payment.objects.all()
  return render(request, 'payment_list.html', {'paymentList':paymentList})

def reserveView(request):
    if request.method == "POST":
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = models.User.objects.filter(UserName=request.session['currentUserName']).first()
            appointment = models.Appointment.objects.create(ClinicId=cd['ClinicId'], ServiceId=cd['ServiceId'], UserName=user, Date=cd['Date'], Time=cd['Time'], Status='Booked')
            return redirect('/clinicsystem/patient_panel/')
    else:
        form = forms.ReserveForm()
    return render(request, 'reserve.html', {'form':form})

def appointmentListView(request):
  appointmentList = models.Appointment.objects.all()
  return render(request, 'appointment_list.html', {'appointmentList':appointmentList})

def serviceListView(request):
  serviceList = models.Service.objects.all()
  return render(request, 'service_list.html', {'serviceList':serviceList})

def notificationListView(request):
  notificationList = models.Notification.objects.all()
  return render(request, 'notification_list.html', {'notificationList':notificationList})

def createClinicView(request):
    if request.method == "POST":
        form = forms.ClinicForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            clinic = models.Clinic.objects.create(Name=cd['Name'], Address=cd['Address'], Contact=cd['Contact'], Availability=True)
            return redirect('/clinicsystem/staff_panel/')
    else:
        form = forms.ClinicForm()
    return render(request, 'create_clinic.html', {'form':form})

def createServiceView(request):
    if request.method == "POST":
        form = forms.ServiceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            service = models.Service.objects.create(ClinicId=cd['ClinicId'], Name=cd['Name'], Price=cd['Price'])
            return redirect('/clinicsystem/staff_panel/')
    else:
        form = forms.ServiceForm()
    return render(request, 'create_service.html', {'form':form})

def createPaymentView(request):
    if request.method == "POST":
        form = forms.CreatePaymentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            appointment = models.Appointment.objects.filter(AppointmentId=cd['AppointmentId'].AppointmentId).first()
            service = models.Service.objects.filter(ServiceId=appointment.ServiceId.ServiceId).first()
            payment = models.Payment.objects.create(AppointmentId=cd['AppointmentId'], DateTime=datetime.now(None), Amount=service.Price)
            return redirect('/clinicsystem/staff_panel/')
    else:
        form = forms.CreatePaymentForm()
    return render(request, 'create_payment.html', {'form':form})

def clinicView(request, clinicId):
    if request.session['currentUserName'] != "":
        clinic = models.Clinic.objects.filter(ClinicId=clinicId).first()
        if request.method == 'POST':
            form = forms.ClinicForm(request.POST, instance=clinic)
            if form.is_valid():
                cd = form.cleaned_data
                if clinic != None:
                    clinic.ClinicId = cd['ClinicId']
                    clinic.Name = cd['Name']
                    clinic.Address = cd['Address']
                    clinic.Contact = cd['Contact']
                    clinic.Availability = cd['Availability']
                    clinic.save()
                    messages.info(request, 'Clinic updated successfully')
                    if request.session['currentUserType'] == 'Patient':
                        return redirect('/clinicsystem/patient_panel/')
                    else:
                        return redirect('/clinicsystem/staff_panel/')
                else:
                    messages.error(request, 'Clinic Id not found', 'errormessage')
            else:
                messages.error(request, 'ERROR')
        else:
            form = forms.ClinicForm(instance=clinic)
    return render(request, 'clinic.html', {'form':form, 'clinicId':clinicId})

def serviceView(request, serviceId):
    if request.session['currentUserName'] != "":
        service = models.Service.objects.filter(ServiceId=serviceId).first()
        if request.method == 'POST':
            form = forms.ServiceForm(request.POST, instance=service)
            if form.is_valid():
                cd = form.cleaned_data
                if service != None:
                    service.ServiceId = cd['ServiceId']
                    service.ClinicId = cd['ClinicId']
                    service.Name = cd['Name']
                    service.Price = cd['Price']
                    service.save()
                    messages.info(request, 'Service updated successfully')
                    if request.session['currentUserType'] == 'Patient':
                        return redirect('/clinicsystem/patient_panel/')
                    else:
                        return redirect('/clinicsystem/staff_panel/')
                else:
                    messages.error(request, 'Service Id not found', 'errormessage')
            else:
                messages.error(request, 'ERROR')
        else:
            form = forms.ServiceForm(instance=service)
    return render(request, 'service.html', {'form':form, 'serviceId':serviceId})

def paymentView(request, paymentId):
    if request.session['currentUserName'] != "":
        payment = models.Payment.objects.filter(PaymentId=paymentId).first()
        if request.method == 'POST':
            form = forms.PaymentForm(request.POST, instance=payment)
            if form.is_valid():
                cd = form.cleaned_data
                if payment != None:
                    payment.PaymentId = cd['PaymentId']
                    payment.AppointmentId = cd['AppointmentId']
                    payment.Amount = cd['Amount']
                    payment.save()
                    messages.info(request, 'Service updated successfully')
                    if request.session['currentUserType'] == 'Patient':
                        return redirect('/clinicsystem/patient_panel/')
                    else:
                        return redirect('/clinicsystem/staff_panel/')
                else:
                    messages.error(request, 'Payment Id not found', 'errormessage')
            else:
                messages.error(request, 'ERROR')
        else:
            form = forms.PaymentForm(instance=payment)
    return render(request, 'payment.html', {'form':form, 'paymentId':paymentId})

def clinicList1View(request):
  clinicList = models.Clinic.objects.all()
  return render(request, 'clinic_list1.html', {'clinicList':clinicList})

def paymentList1View(request):
  paymentList = models.Payment.objects.all()
  return render(request, 'payment_list1.html', {'paymentList':paymentList})

def serviceList1View(request):
  serviceList = models.Service.objects.all()
  return render(request, 'service_list1.html', {'serviceList':serviceList})

