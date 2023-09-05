from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hola(request):
    return HttpResponse("<h1>Bienvenidos</h1>")

def fecha(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)

def template(request):
    data = {"nombre" : "Benja"}
    return render(request, 'index.html', data)

def info(request):
    data = {"id" : 123,
            "nombre": "Clark Kent",
            "email" : "superman@jl.org",
            }
    
    return render(request,'userInfoTemplate.html',data)