from django.shortcuts import render,redirect
from .forms import CarroForm,ClienteForm

# Create your views here.
from .models import Cliente,Aluguel,Carro


def home(request):
    return render(request,"index.html")
 
#Carros

def listar_carro(request):
    carros=Carro.objects.all()
    context = {"carros": carros}
    return render(request,"carro/listar.html",context=context)

def detalhar_carro(request, pk):
    carros = Carro.objects.get(pk=pk)
    context = {"carros": carros}
    return render(request, "carro/detalhar.html", context=context)

def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CarroForm()
            return render(request, "carro/cadastro.html", {'form': form})
    else:
        form = CarroForm()
        return render(request, "carro/cadastro.html", {'form': form})
    
def atualizar_carro(request, pk):
    carros = Carro.objects.get(pk=pk)
    form = CarroForm(instance=carros)
    
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carros)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            return render(request, "carro/atualizar.html", {'form': form})
    else:
        return render(request, "carro/atualizar.html", {'form': form})

def deletar_carro(request, pk):
    carros = Carro.objects.get(pk=pk)

    if carros:
        carros.delete()
        return redirect('/')
    else:
        return render(request, "carro/listar.html", {'msg': "Carro não encontrado"})


#cliente

def listar_cliente(request):
    clientes=Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request,"cliente/listar.html",context=context)

def detalhar_cliente(request, pk):
    clientes = Cliente.objects.get(pk=pk)
    context = {"clientes": clientes}
    return render(request, "cliente/detalhar.html", context=context)

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            form = CarroForm()
            return render(request, "cliente/cadastro.html", {'form': form})
    else:
        form = ClienteForm()
        return render(request, "cliente/cadastro.html", {'form': form})
    
def atualizar_cliente(request, pk):
    clientes = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=clientes)
    
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            return render(request, "cliente/atualizar.html", {'form': form})
    else:
        return render(request, "cliente/atualizar.html", {'form': form})

def deletar_cliente(request, pk):
    clientes = Cliente.objects.get(pk=pk)

    if clientes:
        clientes.delete()
        return redirect('')
    else:
        return render(request, "cliente/listar.html", {'msg': "Cliente não encontrado"})
