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

def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CarroForm()
            return render(request, "carro/cadastrar.html", {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastrar.html", {'form': form})
    
def atualizar_carro(request, pk):
    autor = Carro.objects.get(pk=pk)
    form = CarroForm(instance=carro)
    
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "carro/atualizar.html", {'form': form})
    else:
        return render(request, "carro/atualizar.html", {'form': form})

def deletar_carro(request, pk):
    autor = Carro.objects.get(pk=pk)

    if autor:
        autor.delete()
        return redirect("/")
    else:
        return render(request, "carro/listar.html", {'msg': "Carro não encontrado"})
