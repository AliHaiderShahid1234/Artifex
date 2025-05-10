from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user using email and password
            user = authenticate(request, username=username, password=password)
            
            # If authentication fails, show an error
            if user is not None:
                login(request, user)  # Login the user
                return redirect('home')  # Redirect to home or another page
            else:
                messages.error(request, "Invalid email or password")  # Show error message
        else:
            messages.error(request, "Please fill out the form correctly.")  # Form error message
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})