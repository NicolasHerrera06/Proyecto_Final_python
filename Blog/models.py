from pyexpat import model
from django.db import models

# Create your models here.

class Posteo(models.Model):
    titulo  = models.CharField(max_length=100)
    fecha = models.DateField()
    texto = models.TextField()
    autor = models.CharField(max_length=50) 
    #imagenes = models.ImageField(upload_to="img", null=True)

    def __str__(self):
        return self.titulo

opciones_consultas = [
    [0, "consulta"],
    [1,"reclamo"],
    [2,"sugerencia"],
    [3,"Felicitaciones, la página está muy buena"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre