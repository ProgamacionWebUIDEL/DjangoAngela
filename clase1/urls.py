"""clase1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from libros import views

router = routers.DefaultRouter()
router.register(r'libro', views.LibroVista, 'libro')
router.register(r'Autos', views.AutosVista, 'Autos')
router.register(r'Ropa', views.RopaVista, 'Ropa')
router.register(r'Pelicula', views.PeliculaVista, 'Pelicula')
router.register(r'Zapatos', views.ZapatosVista, 'Zapatos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros',include(router.urls))
]
