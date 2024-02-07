from django.db import models
from .category import Category

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
