from django.db import models
from usuario.models import Usuario
from .livro import Livro

class Compra(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    livro = models.ManyToManyField(Livro, through='CompraLivro')

    def __str__(self):
        return self.user.username