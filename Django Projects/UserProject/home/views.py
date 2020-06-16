from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login/')
    return render(request,'index.htm')

def loginUser(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered Correct Credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect("/")
        else:
            return render(request, 'login.htm')
    
    return render(request,'login.htm')

def logoutUser(request):
    logout(request)
    return redirect('/login/')