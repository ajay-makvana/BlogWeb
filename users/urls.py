from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'users'

urlpatterns = [
    # Login Page
    path('login/',views.login,name='login'),
    # Registration page.
    path('register/', views.register, name='register'),
    #Logout Page
    path('logout/', views.logout, name='logout'),
]