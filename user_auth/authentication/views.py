from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'username doesnt exist')
            return render('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
        
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, 'username already in use')
            return redirect('/register/')
        
        user=User(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('/login/')
    
    return render(request, 'register.html')