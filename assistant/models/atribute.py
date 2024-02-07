from django.db import models

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class AttributeOption(models.Model):
    attribute = models.ForeignKey(Attribute, related_name="options", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_adjustment = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) 

    def __str__(self):
        return f"{self.name} (${self.price_adjustment})"
