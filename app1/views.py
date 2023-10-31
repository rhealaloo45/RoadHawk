from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User
from project1 import settings
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        print(request)
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        print (user)
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            # user.is_active()
            return render(request, "home/home.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    return render(request, 'home/login.html')

def signup(request):
    if request.method == "POST":
            # username = request.POST.get('username')
            username = request.POST['username']
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('home')
        
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('home')
        
            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('home')
            
            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                return redirect('home')
            
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            
            myuser.save()
            
            messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
            
            # messages.success(request,'Registration Successfull')
            
            return redirect('/signin')
    return render(request, 'home/signup.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

@login_required(login_url='signin')
def home(request):
    # login(request)
    # fname = user.first_name
    # fname=fname
    return render(request, 'home/home.html')