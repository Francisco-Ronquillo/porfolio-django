from django.db import models
from django.db.models.fields import DecimalField, CharField, URLField,TextField,DateField
from django.db.models.fields.files import ImageField
import datetime

class Project(models.Model):
    title = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    image = ImageField(upload_to="porfolio/images/")
    url = URLField(blank=True)

class Experience(models.Model):
    institucion_del_curso=CharField(max_length=100)
    descripcion_curso=TextField()
    fecha_curso = DateField(default=datetime.date.today)
    numero_horas=DecimalField(max_digits=5, decimal_places=2)


class Relacion(models.Model):
    descripcion = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.descripcion

class Referencias_laborales(models.Model):
    nombre_test=CharField(max_length=30)
    relacion = models.ma(Relacion,on_delete=models.CASCADE)
    telefono=CharField(max_length=10)
    correo=CharField(max_length=80)
    descripcion=models.TextField()
    def __str__(self):
        return f"{self.nombre_test} - {self.relacion.descripcion}"
