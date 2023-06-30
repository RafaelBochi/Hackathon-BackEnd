from django.contrib import admin

from .models import Autor, Genero, Livro, Carrinho, CarrinhoLivro, Compra, CompraLivro

admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(Autor)
admin.site.register(Carrinho)
admin.site.register(CarrinhoLivro)
admin.site.register(Compra)
admin.site.register(CompraLivro)
