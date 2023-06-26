from django.contrib import admin

from .models import Autor, Genero, Livro

admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(Autor)
