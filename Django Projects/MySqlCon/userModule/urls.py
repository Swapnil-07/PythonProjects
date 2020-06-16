from django.contrib import admin
from django.urls import path, include
from userModule import views

urlpatterns = [
    path('home/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
]