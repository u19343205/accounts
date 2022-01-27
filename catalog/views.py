from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home.html")

def logout(request):
    return render(request, "{% url 'login' %}")

