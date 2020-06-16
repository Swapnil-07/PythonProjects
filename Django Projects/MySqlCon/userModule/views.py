from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home.htm')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already Taken')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            user.save()
            return redirect('/home')
    return render(request, 'register.htm')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            # messages.info(request, 'Invalid Credentials')
            print('invalid credentials')
            return redirect('/login')
    return render(request, 'login.htm')

def logout(request):
    auth.logout(request)
    return redirect('/home')
