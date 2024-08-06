from django.db import models

# Create your models here.
class Prueba(models.Model):
    si = models.CharField(primary_key=True,max_length=501)
    atributo = models.CharField(max_length=501)