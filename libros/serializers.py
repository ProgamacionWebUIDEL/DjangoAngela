from rest_framework import serializers 
from .models import Libro
from .models import Autos 
from .models import Ropa
from .models import Pelicula
from .models import Zapatos

class LibroSerializable(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields=(
            'titulo',
            'autor',
            'numero_paginas'
        )

class AutosSerializable(serializers.ModelSerializer):
    class Meta:
        model=Autos
        fields=(
            'Marca',
            'cilindraje',
            'numero_paginas'
        )

class RopaSerializable(serializers.ModelSerializer):
    class Meta:
        model:Ropa
        fields=(
            'Marca',
            'Precio',
            'numero_paginas'
        )

class PeliculaSerializable(serializers.ModelSerializer):
    class Meta:
        model:Pelicula
        fields=(
            'Nombre',
            'Año',
            'Duracion',
            'numero_paginas'
        )

class ZapatosSerializable(serializers.ModelSerializer):
    class Meta:
        model:Zapatos
        fields=(
            'Mterial',
            'Diseño',
            'numero_paginas'
        )
