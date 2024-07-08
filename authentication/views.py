from django.shortcuts import render, redirect
from .forms import SignUpForms
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_auth = authenticate(request,username = username,password = password)
        if is_auth:
            login(request,is_auth)
            return redirect("home:home")
    return render(request,"authentication/login.html")
def signup(request):
    form = SignUpForms()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passowrd2 = request.POST.get("password2")
        form.username = username
        form.email = email
        form.password = password
        form.password2 = passowrd2
        form = SignUpForms(request.POST)
  
        if form.is_valid():
            form.save()
            return redirect("auth:signin")
    return render(request,"authentication/register.html")