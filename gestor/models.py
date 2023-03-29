from django.db import models

# Create your models here.
class producto(models.Model):
    producto=models.CharField(max_length=30)
    descripccion=models.CharField(max_length=30)
    precio=models.IntegerField()


class categorias(models.Model):
    nombre=models.CharField(max_length=20)
    descripccion=models.CharField(max_length=30)


    