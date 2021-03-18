from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data("username")
#         password = form.cleaned_data("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('index')
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)
from .forms import NewUserForm
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Succesfull")
            return redirect('index')
        messages.error(request, "Unsuccessful registration. Invalid Information")
    form = NewUserForm
    context = {
        "register_form": form,
    }
    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    form = AuthenticationForm()
    return render(request, 'users/login.html', context={"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "you have successfully logged out")
    return redirect('index')
