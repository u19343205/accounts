from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home.html") #makes the index set to home so it is the first url


def logout(request):
    return render(request, "{% url 'login' %}") #loop the logout to login page 

