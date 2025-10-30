from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60)
    cuerpo = models.TextField()
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"({self.id}){self.titulo}"