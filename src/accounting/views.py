from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import SignUpForm


def SignupView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'Successfully logged in.')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def LogoutView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
