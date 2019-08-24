from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User
# Create your views here.
# an iniatl view this is what you will see when you acsess this website
def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'success.html')
        else:
            messages.info(request,'invaild login')
            return redirect("/login")
    else:
        return render(request,'login.html')