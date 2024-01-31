from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Clinic, Appointment, Notification, Service, Payment

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.login(username, password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        email = request.POST['email']
        usertype = request.POST['usertype']
        user = User.register(username, password, name, email, usertype)
        return redirect('login')
    else:
        return render(request, 'register.html')

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')


