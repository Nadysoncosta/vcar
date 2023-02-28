from django.db import models

# Create your models here.
class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True,unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    data_nascimento=models.DateField()
    endereco = models.CharField(max_length=200)
    #idade=pass
    def __str__(self):
        return self.nome

class Carro(models.Model):
    placa = models.CharField(max_length=15,primary_key=True,unique=True)
    ano = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    data_compra = models.DateField()
    status = models.CharField(max_length=15)
    

class Aluguel(models.Model):
    codigo=models.CharField(max_length=15,primary_key=True, unique=True)
    data_aluguel=models.DateField()
    data_entrega=models.DateField()
    diaria=models.DecimalField(max_digits = 10, decimal_places = 2)
    placa_carro=models.ForeignKey(Carro,on_delete=models.CASCADE)
    cpf_cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
