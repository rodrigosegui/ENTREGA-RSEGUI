from django.urls import path
from Appsma.views import *


urlpatterns = [
    path('veralojamientos/', ver_alojamientos ),
    path('agregaralojamiento/', agregaralojamiento),
    path('vervehiculos/', ver_vehiculos),
    path('verhuesped/', ver_huepedes),
    path('buscaralojamiento/',buscaralojamiento),
    path('resultados/', resultados),
]