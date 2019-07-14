from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

#########################################
def signup(request):

    if request.method == 'POST':
        #The user wants to sign up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'userlogin/signup.html', {'error': 'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'userlogin/signup.html', {'error':'Passwords do not match'})
    else:
        #The user wants to enter info
        return render(request, 'userlogin/signup.html')

#########################################
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'userlogin/login.html', {'error': 'Username or password is incorrect.'})
    else:
        return render(request, 'userlogin/login.html')

#########################################
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')