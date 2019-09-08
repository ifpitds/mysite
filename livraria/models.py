from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    assunto = models.CharField(max_length=30)
    editora = models.CharField(max_length=30)
    isbn = models.CharField(max_length=50)
    ano_publicacao = models.DateField()


def __str__(self):
    return self.titulo
