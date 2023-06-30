from django.db import models

from .autor import Autor
from .genero import Genero

class Livro(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    author = models.ForeignKey(Autor, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} - {self.price}"
