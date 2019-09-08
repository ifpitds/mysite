from django.contrib import admin

# Register your models here.

from .models import Livro


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','assunto','editora','isbn','ano_publicacao')

admin.site.register(Livro,LivroAdmin)
