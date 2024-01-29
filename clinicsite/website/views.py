from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Clinic, Appointment, Notification, Service, Payment

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'کاربری با این مشخصات یافت نشد'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        user = User.register(username, password, name, email, usertype)
        if user is None:
            return render(request, 'register.html', {'error': 'نام کاربری قبلا انتخاب شده است'})
        return redirect('login')
    else:
        return render(request, 'register.html')
    
@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html', {
        'username': request.user.username,
    })
