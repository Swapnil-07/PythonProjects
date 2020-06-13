from django.contrib import admin
from django.urls import path, include
from crud import views

urlpatterns = [
    path('', views.showEmp),
    path('create/', views.createEmp),
    path('show/', views.showEmp),
    path('edit/<int:id>', views.editEmp),
    path('update/<int:id>', views.updateEmp),
    path('delete/<int:id>', views.deleteEmp),
]