from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.name