from django.urls import path
from . import views
#this is the url that you need to check for login

urlpatterns = [
    path( '', views.login, name = 'login'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout, name = 'logout'),
    path('register', views.register, name = 'register'),
]