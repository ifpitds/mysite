from django.db import models

# Create your models here.
class Apartamento(models.Model):
    numero = models.PositiveIntegerField()
    qtdQuartos = models.PositiveIntegerField()
    proprietario = models.CharField(max_length=30)
    valorCondominio = models.DecimalField(decimal_places=2,max_digits=9)


def __str__(self):
    return self.numero
