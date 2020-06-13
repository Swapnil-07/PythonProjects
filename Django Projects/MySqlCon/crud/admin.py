from django.contrib import admin
from .models import Employee

# Register your models here.
# admin.site.register(Employee)           #Model registration to display in Admin Panel

# In case you want Complete coloumn names to show in Admin Panel

class showColumn(admin.ModelAdmin):
    list_display=('empName', 'empEmail', 'empPhone')

    # def has_delete_permission(self, request, obj = None):  # Code to Hide DELETE Control from Admin Panel
    #     return False

    # def has_add_permission(self, request):       # Code to Hide ADD Control from Admin Panel
    #     return False

    # def make_active(modeladmin, request, queryset):                   #Code to Add "Menu" in dropDown of Admin Panel along Delete Menu
    #     queryset.update(is_active = 1) 
    #     messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 
  
    # def make_inactive(modeladmin, request, queryset): 
    #     queryset.update(is_active = 0) 
    #     messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!") 
  
    # admin.site.add_action(make_active, "Make Active") 
    # admin.site.add_action(make_inactive, "Make Inactive")

admin.site.register(Employee,showColumn)



