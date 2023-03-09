from django.db import models
# from datetime import datetime

# Create your models here.
class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True,unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    data_nascimento=models.DateField()
    endereco = models.CharField(max_length=200)
    #idade=models.DateField(models.DateTimeField(auto_now_add=True)-data_nascimento)
    #datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    def __str__(self):
        return "{} - {}".format(self.nome,self.cpf)

class Carro(models.Model):
    codigo =models.BigAutoField(primary_key=True,unique=True)
    placa = models.CharField(max_length=15)
    ano = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    data_compra = models.DateField()
    status = models.CharField(max_length=15)
    
    def __str__(self):
        return "{}-{}".format(self.modelo,self.ano)

class Aluguel(models.Model):
    codigo=models.AutoField(primary_key=True,unique=True)
    data_aluguel=models.DateField(blank=True)
    data_entrega=models.DateField(blank=True)
    diaria=models.DecimalField(max_digits = 10, decimal_places = 2)
    placa_carro=models.ForeignKey(Carro,on_delete=models.NOT_PROVIDED)
    cpf_cliente=models.ForeignKey(Cliente,on_delete=models.NOT_PROVIDED)

    def __str__(self):
        return self.codigo