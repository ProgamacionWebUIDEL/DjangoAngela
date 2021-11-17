from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo=models.CharField(max_length=120, help_text='title of message.')
    autor=models.CharField(max_length=120, help_text='autor of message.')
    numero_paginas=models.IntegerField(max_length=1000,help_text='numero de paginas de textos')

class Autos(models.Model):
    marca=models.CharField(max_length=200,help_text='Ingrese marca de vehiculo')
    cilindraje=models.FloatField(help_text='Ingrese el cilindraje')

class Ropa(models.Model):
    marca=models.CharField(max_length=200,help_text='Ingrese la marca de Ropa')
    Precio=models.FloatField(help_text='Ingrese el precio')
    Diseñador=models.FloatField(help_text='Ingrese el nombre del diseñador')

class Pelicula(models.Model):
    Nombre=models.CharField(max_length=200,help_text='Ingrese el nombre de la pelicula')
    Año=models.FloatField(help_text='Ingrese el año de la pelicula')
    Duracion=models.FloatField(help_text='Ingrese el tiempo que dura la pelicula')

class Zapatos(models.Model):
    material=models.CharField(max_length=200,help_text='Ingrese el nombre del material')
    Diseño=models.FloatField(help_text='Ingrese el nombre del diseño')


    