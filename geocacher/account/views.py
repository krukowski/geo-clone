from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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
                return redirect(request, next)
            else:
                message = "Your account is not active."
        else:
            message = "Incorrect username and/or password."
    next = request.GET.get('next')
    return render(request, 'account/auth.html',{'message':message, 'username':username, 'next':next})
