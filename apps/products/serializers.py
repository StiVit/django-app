from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    in_stock = serializers.BooleanField(read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "amount", "in_stock"]