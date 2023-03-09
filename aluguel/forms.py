from django.forms import ModelForm
from .models import Cliente,Carro,Aluguel

class CarroForm(ModelForm):
   model = Carro
   fields = "__all__"


class ClienteForm(ModelForm):
    model = Cliente
    fields = "__all__"

class AluguelForm(ModelForm):
    model = Aluguel
    fields = "__all__"