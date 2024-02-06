# assistant/models.py

from django.db import models


class Comida(models.Model):
    comida = models.CharField(max_length=255)

    def __str__(self):
        return self.comida

class Carrinho(models.Model):
    token = models.CharField(max_length=255)
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    class Meta:
        unique_together = ('token', 'comida')

