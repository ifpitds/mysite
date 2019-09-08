from django.db import models

# Create your models here.

class Compras(models.Model):
    nome = models.CharField(max_length=30)
    descricaoProduto = models.CharField(max_length=200)
    unidadeCompra = models.CharField(max_length=30)
    qtdPrevistoMes = models.DecimalField(max_digits=7, decimal_places=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    precoMaximo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
