from django.shortcuts import render, redirect
from crud.models import Employee
from crud.forms import EmployeeForm

# Create your views here.

def createEmp(request):
    if request.method == 'POST' :
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.htm', {'form':form})

def showEmp(request):
    employees = Employee.objects.all()   # object is defined in Model as objects = models.Manager()
    return render(request, "show.htm", {'employees':employees}) #from {key:value} pair only key will be used in template to itterate

def editEmp(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.htm", {'employee':employee})

def updateEmp(request, id=0):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.htm", {'employee':employee})

def deleteEmp(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


    