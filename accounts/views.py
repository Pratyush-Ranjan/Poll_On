from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')
def signup_view(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/home")
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                userObj = form.cleaned_data
                username = userObj['username']
                email =  userObj['email']
                password =  userObj['password']
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return HttpResponseRedirect("/home")
                else:
                    raise forms.ValidationError('Looks like a user with that email or username already exists')
        else:
            form = UserRegistrationForm()
        return render(request, 'accounts/signup.html', {'user_form' : form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")