from django.contrib import admin
from .models import Libro
from .models import Autos
from .models import Ropa 
from .models import Pelicula
from .models import Zapatos
# Register your models here.
admin.site.register(Libro)
admin.site.register(Autos)
admin.site.register(Ropa)
admin.site.register(Pelicula)
admin.site.register(Zapatos)
