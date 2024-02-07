from django.db import models
from .menu import MenuItem
from .atribute import AttributeOption

class CustomizedItem(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    options = models.ManyToManyField(AttributeOption, blank=True)

    def __str__(self):
        return f"Customized {self.item.name}"
