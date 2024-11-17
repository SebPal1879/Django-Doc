from django.shortcuts import render
from . import models
# Create your views here.
def calentamiento(request):
    contexto = models.qq.objects.first()
    return render(request,"calentamiento/cal.html",{"contexto":contexto})
    