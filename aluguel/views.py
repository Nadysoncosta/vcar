from django.shortcuts import render

# Create your views here.
from .models import Cliente,Aluguel,Carro
import datetime

def home(request):
    return render(request,"home.html")
 
#Carros

def listar_carro(request):
    carros=Carro.objects.all()
    context = {"carros": carros}
    return render(request,"carro/listar.html",context)

def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    context = {"carro": carro}
    return render(request, "carro/detalhar.html", context)