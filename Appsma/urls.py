from django.urls import path
from Appsma.views import *


urlpatterns = [
    path('veralojamientos/', ver_alojamientos, name="Alojamientos" ),
    path('agregaralojamiento/', agregaralojamiento, name="Nuevos"),
    path('vervehiculos/', ver_vehiculos, name="Vehiculos"),
    path('verhuesped/', ver_huepedes, name="Clientes"),
    path('buscaralojamiento/',buscaralojamiento, name = "Busca tu alojamiento"),
    path('resultados/', resultados, name="Resultados"),
    path('inicio/', inicio, name="Inicio"),
    path('nosotros/', nosotros, name="Nosotros"),
    
]