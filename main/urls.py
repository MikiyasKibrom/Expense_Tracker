from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.main, name= 'home'),
    path('home/', views.main, name='home2'),
    path('', include('django.contrib.auth.urls')),
]