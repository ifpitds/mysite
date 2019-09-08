from django.db import models

# Create your models here.

class Anuncio(models.Model):
    cliente = models.CharField(max_length=30)
    textoTitulo = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    textoAnuncio = models.CharField(max_length=200)
    nomeContato = models.CharField(max_length=30)
    telefone = models.CharField(max_length=15)
    secao = models.CharField(max_length=30)
    tipoAnuncio = models.CharField(max_length=30)


def __str__(self):
    return self.cliente



