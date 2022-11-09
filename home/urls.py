from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.process_contact_form, name='contact'),
    
]