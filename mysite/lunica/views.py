from django.shortcuts import render
from .models import lunica

# Create your views here.
def vistaluna(request):
    objetico = lunica.objects.first()
    return render(request,"lunica/lunuwu.html",{"contextico":objetico})