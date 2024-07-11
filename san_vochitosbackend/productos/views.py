from django.shortcuts import render
from .models import Project 
# Create your views here.

def productos (request):
    projects = Project.objects.all()    
    return render(request, "productos/productos.html", {'projects': projects})
 