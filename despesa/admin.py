from django.contrib import admin

# Register your models here.

from .models import Despesa


# Register your models here.

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipo_despesa', 'descricao','forma_pagamento', 'vencimento', 'quitado')

admin.site.register(Despesa, DespesaAdmin)
