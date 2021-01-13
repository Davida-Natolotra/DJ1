from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .decorators import unauthenticated_user

# Create your views here.

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')


def accounts(request):
    return render(request,'accounts/account.html')

