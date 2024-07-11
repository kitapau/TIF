from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):    
    return render(request, "core/index.html") 


def locales (request):    
    return render(request, "core/locales.html")

def contacto (request):    
    return render(request, "core/contacto.html")