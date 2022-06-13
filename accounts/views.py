from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST.get('password2','default value')
        if password1 == password2:
            if User.object.filter(username=username).exists:
                print('username taken')
            else:
                user = User.objects.create_user(
                username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print('password do not match')
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request, "register.html")


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("login.html")
    else:
        return render(request, 'login.html')   