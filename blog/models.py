from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_nac = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    cuerpo = models.TextField()
    fecha = models.DateField(null=True, blank=True)
    imagen = models.ImageField(null=True, upload_to='blog/media')

    def __str__(self):
        return f"({self.id}){self.titulo}"