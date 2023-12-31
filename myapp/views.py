from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
# Create your views here and these are redirected from urls.py and will be redirected html
def index(request):
    opt = Feature.objects.all()
    return render(request,"index.html", dict(option=opt))
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2= request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password is not matched')
            return redirect('register')
    else:
        return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid password or username')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    return render(request, "counter.html")

