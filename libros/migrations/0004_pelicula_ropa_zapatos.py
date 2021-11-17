# Generated by Django 3.2.9 on 2021-11-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_autos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(help_text='Ingrese el nombre de la pelicula', max_length=200)),
                ('Año', models.FloatField(help_text='Ingrese el año de la pelicula')),
                ('Duracion', models.FloatField(help_text='Ingrese el tiempo que dura la pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Ingrese la marca de Ropa', max_length=200)),
                ('Precio', models.FloatField(help_text='Ingrese el precio')),
            ],
        ),
        migrations.CreateModel(
            name='Zapatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(help_text='Ingrese el nombre del material', max_length=200)),
                ('Diseño', models.FloatField(help_text='Ingrese el nombre del diseño')),
            ],
        ),
    ]
