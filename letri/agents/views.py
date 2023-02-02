from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from main.forms import BodyForm
from main.views import add_body
# Create your views here.

def login_user(request):
    form2 = BodyForm()
    if request.method =="POST":
        try:
            username = request.POST['username']
        except:
            return add_body(request)

        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Error login..."))
            return redirect('login')
    else:
        return render(request,"registration/login.html",{"form2":form2})

def logout_user(request):
    logout(request)

    messages.success(request, ("logout..."))
    return redirect('home')

def register_user(request):
    if request.method =="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user = authenticate(username=username, password=password)
             login(request,user)
             messages.success(request, ("registration done..."))
             return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request,'registration/register_user.html',{'form':form})
