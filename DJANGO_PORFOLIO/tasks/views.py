from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
def signup(request):
    if request.method=='GET':
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            # register user
            try:
                user=User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect('porfolio:home')
            except IntegrityError:
                return render(request, "signup.html", {"form": UserCreationForm, 'error':'User ya existe'})
        else:
            return render(
                request,
                "signup.html",
                {"form": UserCreationForm, "error": "Password do not match"},
            )
def base(request):
    return render( request,"base.html")

def signin(request):
    print('enviando formulario')
    if request.method=='GET':
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, "signin.html", {"form": AuthenticationForm,'error':'Usuario o Contraseña es incorrecto'})
        else:
            login(request,user)
            return redirect('porfolio:home')


def signout(request):    
    logout(request)
    return redirect('tasks:base')
