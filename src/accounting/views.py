from django.shortcuts import render, redirect

from .forms import SignUpForm


def SignupView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def HomeView(request):
    return render(request, 'home.html')
