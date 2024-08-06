from django.shortcuts import render,get_object_or_404
from .models import Prueba
# Create your views here.
def xd(request):
    #modelo = Prueba.objects.first()
    modelo = get_object_or_404(Prueba, pk=0)
    return render(request,"fast/sisas.html",{"contexto":modelo})
