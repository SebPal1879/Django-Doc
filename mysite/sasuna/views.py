from django.shortcuts import render
from .models import sasunita

# Create your views here.
def sus(request):
    objeto = sasunita.objects.first()
    return render(request,"sasuna/importa.html",{"objeto":objeto})

