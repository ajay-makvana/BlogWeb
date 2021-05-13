from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import login
import blog.urls
# Create your views here.

def register(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName Already Taken')
                return render(request,'users/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Registered')
                return render(request,'users/register.html')
            else:
                new_user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                new_user.save()
                print(new_user)
                return redirect('blog:index')
        else:
            messages.info(request,'Password Not Matched')

    return render(request,'users/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("blog:index")
        else:
            messages.info(request,'Invalid Username or Password')
    return render(request,'users/login.html')

def logout(request):
    auth.logout(request)
    return redirect("blog:index")