from django.forms import ModelForm
from .models import Cliente,Carro,Aluguel

class CarroForm(ModelForm):
    class Meta:
      model = Carro
      fildes = ['placa','marca','ano','modelo','data_compra','status']


class ClienteForm(ModelForm):
    class Meta:
      model = Cliente
      fildes = ['cpf','nome','telefone','data_nascimento', 'endereco']


class AluguelForm(ModelForm):
    class Meta:
      model = Aluguel
      fildes = ['codigo','data_aluguel','data_entrega', 'diaria','para_carro','cpf_cliente']