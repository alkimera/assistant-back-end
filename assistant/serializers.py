from rest_framework import serializers
from .models import ItemCardapio

class ItemCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCardapio
        fields = '__all__'

