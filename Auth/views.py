from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import LoginForm, RegisterUserForm


def logout_view(request):
    logout(request)
    return redirect('main-page')


def login_view(request):
    # Account login function. Performs data validation on the form and performs a login.
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('main-page')
                    else:
                        return render(request, 'Auth/page-login.html', {'message': 'User is not active!'})
                else:
                    return render(request, 'Auth/page-login.html', {'message': 'User dos not exist!'})
            else:
                return render(request, 'Auth/page-login.html', {'message': 'The given input is not correct!'})
        else:
            form = LoginForm()
            return render(request, 'Auth/page-login.html', {'form': form})
    return redirect('main-page')


def register(request):
    # Registration function. Accepts a request from the front and submits it to the form.
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("main-page")
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = RegisterUserForm()
        return render (request=request, template_name="Auth/page-create-account.html", context={"register_form":form})
    return redirect('main-page')

def index(request):
    return HttpResponse("Successfully")
