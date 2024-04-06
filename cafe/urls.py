from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('home/', views.home, name='home'),
    path('order/', views.order_page, name='order_page'),
    path('register/', views.register, name='register'),
]
