from django.shortcuts import render
from . import models
# Create your views here.
def generica(request):
    contexto = models.generica.objects.first()
    return render(request,"generica1/gen.html",{"contexto": contexto})