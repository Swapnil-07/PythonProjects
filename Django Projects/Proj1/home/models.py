from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    bio = models.TextField()
    date = models.DateField()

        #It is to change the name of Contacts/Model to Self Name in DB/Admin Panel
    def __str__(self):
        return self.name
    
# Swapii - python manage.py makemigration --- to create a migration file, ready to make migration

# Swapii - python manage.py migrate --- to actully craete Database Schema having model tables




# PS E:\PracProjects\PythonProjects\Django Projects\Proj1> python manage.py shell

# >>> from home.models import Contact
# >>> Contact.objects.all()

# >>> temp = Contact.objects.filter(name="Swapnil")[0]
# >>> temp.email = "swapiirocker@gmail.com"
# >>> temp.save()
# >>> Contact.objects.all()[0].email        
# 'swapiirocker@gmail.com'
# >>> Contact.objects.all().first()                                      
# <Contact: Swapnil>
# >>> Contact.objects.all().last() 
# <Contact: HCL Technologies>
# >>> Contact.objects.filter(bio__startswith="I am")
# <QuerySet [<Contact: Hello World>, <Contact: Killer bags>, <Contact: HP>, <Contact: HCL Technologies>]>