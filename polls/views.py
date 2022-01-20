from django.shortcuts import render

#DataFlair #Views #TemplateInheritance
# Create your views here.
def home(request):
    return render(request, 'base.html')

def other(request):
    context = {
    'k1': 'Welcome to the Second page',
    }
    return render(request, 'home.html', context)

import datetime
def about(request):
    time = datetime.datetime.now()
    return render(request, 'home.html',{'time': time})