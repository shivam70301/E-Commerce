from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.


def home(request):
    products = Product.objects.all() 
    return render (request, 'home.html',{'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password )

        if user is not None :
            login(request,user)
            messages.success(request, "🚀 You’re in! Let’s turn your wishlist into reality.")
            return redirect('home') 
        else:
            messages.success(request, "🕵️Error mystery in progress. Retry while we investigate!")
            return redirect('login')
    else:  
        return render (request, 'login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request, "🎒Journey paused. Don’t worry, your favorites are safe with us")
    return redirect('home')
        
#User Registration
def register_user(request):
    messages.success(request,"✨ You’re one step away from something amazing. Let’s get you started!")
    return render(request, 'register.html')

#🌟 Account created. Adventures in shopping await you!