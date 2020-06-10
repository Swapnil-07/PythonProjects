from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1' : 'This is Sent as Variable',
        'variable2' : 'This is Swapnil in Front OF You'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is Home Page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is About Page')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is Services Page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')

        contact = Contact(name=name, email=email, bio=bio, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent !')

    return render(request, 'contact.html')
    # return HttpResponse('This is Contact Us Page')
