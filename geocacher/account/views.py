from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

def login_user(request):
    message = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = "Successfully logged in!"
                next = request.POST.get('next')
                if not next:
                    next = '/'

                return HttpResponseRedirect(next)
            else:
                message = "Your account is not active."
        else:
            message = "Incorrect username and/or password."
    next = request.GET.get('next')
    return render(request, 'account/auth.html',{'message':message, 'username':username, 'next':next})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    message = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            User.objects.create_user(username,email,password)
        except IntegrityError as e:
            return render(request, 'account/register.html',{'message':str(e)})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                message = "Something went wrong."
        else:
            message = "Something went wrong."
        
    return render(request, 'account/register.html',{'message':message})


def user_profile(request, name):
    return render(request, 'caches/profile.html', {"name":name})


