from django.contrib import admin

# Register your models here.

from .models import Apartamento


# Register your models here.
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'qtdQuartos', 'proprietario', 'valorCondominio')


admin.site.register(Apartamento, ApartamentoAdmin)
