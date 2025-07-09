from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
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
            messages.success(request, "  You’re in! Let’s turn your wishlist into reality.🚀 ")
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
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            #Authenticate
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "🌟 Account created. Adventures in shopping await you!")
            return redirect('home')
        else:
             messages.success(request,"Something wrong!!!")
             return redirect('home')
        
    else:
         return render(request, 'register.html', {'form':form})

#