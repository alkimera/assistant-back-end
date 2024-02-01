from django.db import models

class ItemCardapio(models.Model):
    categoria = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome