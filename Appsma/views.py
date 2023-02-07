from django.shortcuts import render
from Appsma.models import *
from Appsma.forms import *
# Create your views here.

def inicio(request):

    return render(request,"Appsma/inicio.html")

def ver_alojamientos(request):

    todas = Alojamientos.objects.all() #sacando todas los alojamientos de la base de datos

    return render(request,"veralojamientos.html", {"todas":todas})

def ver_huepedes(request):

    return render(request,"Appsma/verhuespedes.html")

def ver_vehiculos(request):
    
    return render(request,"Appsma/vervehiculos.html")


def agregaralojamiento(request):

    if request.method == 'POST':
        miFormulario = AlojamientosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            alojamientos = Alojamientos(nombreA=informacion["nombreA"],habitaciones=informacion["habitaciones"], capacidad=informacion["capacidad"],precioxdia=informacion["precioxdia"])
            alojamientos.save()
            return render(request, "veralojamientos.html")
        
    else:
        miFormulario = AlojamientosFormulario()

    return render(request, "alojamientoformulario.html", {"miFormulario": miFormulario})

def buscaralojamiento(request):
    return render(request, "buscaralojamiento.html")

def resultados(request):

    nombreAbusqueda = request.GET["nombreA"]
    resultadosnombreA = Alojamientos.objects.filter(nombreA__icontains=nombreAbusqueda)
    return render(request, "resultados.html" , {"info1":nombreAbusqueda, "info2":resultadosnombreA})

