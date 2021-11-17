from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LibroSerializable
from .serializers import AutosSerializable
from .serializers import RopaSerializable
from .serializers import PeliculaSerializable
from .serializers import ZapatosSerializable
from .models import Libro
from .models import Autos
from .models import Ropa 
from .models import Pelicula
from .models import Zapatos
# Create your views here.
class LibroVista(viewsets.ModelViewSet):
    serializer_class:LibroSerializable
    queryset=Libro.objects.all()
class AutosVista(viewsets.ModelViewSet):
    serializer_class:AutosSerializable
    queryset=Autos.objects.all()
class RopaVista(viewsets.ModelViewSet):
    serializer_class:RopaSerializable
    queryset=Ropa.objects.all()
class PeliculaVista(viewsets.ModelViewSet):
    serializer_class:PeliculaSerializable
    queryset=Pelicula.objects.all()
class ZapatosVista(viewsets.ModelViewSet):
    serializer_class: ZapatosSerializable
    queryset=Zapatos.objects.all()
