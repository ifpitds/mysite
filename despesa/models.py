from django.db import models

# Create your models here.
class Despesa(models.Model):

     data_criacao = models.DateField()
     tipo_despesa = models.CharField(max_length=30)
     descricao = models.CharField(max_length=250)
     forma_pagamento = models.CharField(max_length=30)
     vencimento = models.DateField()
     quitado = models.BooleanField()

def __str__(self):
     return str(self.data_criacao)
