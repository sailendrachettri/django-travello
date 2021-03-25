from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        # right hand side: same as name field in the html file name
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:

            if User.objects.filter(username=username):
                print('Username Taken')  # Print message in console - developer
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                print('Email Taken')
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('Password not match!')
            messages.info(request, 'Password not match')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username, password') 
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
        
