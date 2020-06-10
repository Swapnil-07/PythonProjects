from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.htm')

def login(request):
    return render(request,'login.htm')

def logout(request):
    return render(request,'logout.htm')
