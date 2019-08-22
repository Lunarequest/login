from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# an iniatl view this is what you will see when you acsess this website
def index(request):
    return HttpResponse("your at the login page")