from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add-project/', views.addProject, name='addProject'),
    path('<int:pk>/', views.portfolio_details, name='portfolio_details'),
    
]