from django.shortcuts import render
from .models import testdoc
# Create your views here.

def iterar(request):
    objeto = testdoc.objects.first()
    objeto.entero += 1
    objeto.save()
    return render(request,"test_docs/iterar.html",{"context": objeto})
