from django.db import models

from usuario.models import Usuario
from .livro import Livro

class Carrinho(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    livro = models.ManyToManyField(Livro, through='CarrinhoLivro')
