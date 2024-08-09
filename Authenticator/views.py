from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_user(request):
    args = {}

    # Check if user already logged in
    if request.user.is_authenticated:
        messages.success(request, ("Already logged in!"))
        return redirect('home')

    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Incorrect username or password."))
            return redirect('login_user')
    else:
        return render(request, 'authenticator/login.html', args)

def register_user(request):
    args = {}

    # Check if user already logged in
    if request.user.is_authenticated:
        messages.success(request, ("Already logged in!"))
        return redirect('home')

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, ("Registered Successfully. Try logging in."))
            return redirect('home')
        else:
            messages.success(request, ("Error with your form."))
            return redirect('register_user')
    else:
        form = UserCreationForm()
        args['form'] = form
        return render(request, 'authenticator/register.html', args)

def user_home(request):
    args = {}

    return render(request, 'authenticator/user_home.html', args)

def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out successfully."))
    return redirect('home')