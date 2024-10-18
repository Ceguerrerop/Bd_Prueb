from django.db import models

# Create your models here.


class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    imagen = models.ImageField(upload_to='imagenes/')