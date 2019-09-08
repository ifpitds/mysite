from django.contrib import admin

# Register your models here.

from .models import Compras

# Register your models here.
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricaoProduto', 'unidadeCompra', 'qtdPrevistoMes', 'preco', 'precoMaximo')

admin.site.register(Compras, ComprasAdmin)


