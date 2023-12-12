from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html", {'success': "Registration successful. Please login."}) #*changee this it lead the user straight to the homepage after signup/register
        else:
            error_message = form.errors.as_text()
            return render(request, "register.html", {'error': error_message})

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dashboard")  #*do this for line 10 as well
        else:
            return render(request, "login.html", {'error': "Invalid credentials. Please try again."})

    return render(request, "login.html")

