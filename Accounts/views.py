from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')
  
def register(request):
    if request.method == 'POST':
        user_forms = UserRegistrationForm(request.POST)
        if user_forms.is_valid():
            #creat a new user object butavoid saving it yet
            new_user = user_forms.save(commit=False)

            new_user.set_password(
                user_forms.cleaned_data['password'])
                #save user object 
            new_user.save()
            return redirect('login')
    else:
        user_forms = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_forms': user_forms})

def login_user(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, ("yuo have been logged_in..."))
            return redirect('prediction')
        else:
            # messages.success(request, ("there was an error logged_in, please try agen..."))
            return redirect('login')
    else:
        return render(request, "registration/login.html")


def logout_user(request):
    logout(request)
    # messages.success(request, (" logged_out ..."))
    return redirect('home')    



