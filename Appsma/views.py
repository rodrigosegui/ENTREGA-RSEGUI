from django.shortcuts import render
from Appsma.models import *
from Appsma.forms import *
from django.http import HttpResponse
# Create your views here.

def inicio(request):

    return render(request,"inicio.html")

def nosotros(request):

    return render(request,"nosotros.html")

def ver_alojamientos(request):

    todas = Alojamientos.objects.all() #sacando todas los alojamientos de la base de datos

    return render(request,"veralojamientos.html", {"todas":todas})

def ver_huepedes(request):

    return render(request,"verhuespedes.html")

def ver_vehiculos(request):
    
    return render(request,"vervehiculos.html")


def agregaralojamiento(request):

    if request.method == 'POST':
        miFormulario = AlojamientosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alojamientos = Alojamientos(nombreA=informacion["nombreA"],habitaciones=informacion["habitaciones"], capacidad=informacion["capacidad"],precioxdia=informacion["precioxdia"])
            alojamientos.save()
            return render(request, "inicio.html")
        
    else:
        miFormulario = AlojamientosFormulario()

    return render(request, "agregaralojamiento.html", {"miFormulario": miFormulario})

def buscaralojamiento(request):
    return render(request, "buscaralojamiento.html")

def resultados(request):

    capacidadbusqueda = request.GET["capacidad"]
    resultadoscapacidad = Alojamientos.objects.filter(capacidad__icontains=capacidadbusqueda)
    return render(request, "resultados.html" , {"info1":capacidadbusqueda, "info2":resultadoscapacidad})


