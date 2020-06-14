from rest_framework import serializers
from core.models import Product, Provider, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only = ('id', 'created_at', 'updated_at',)


class ProviderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Provider
        fields = ('id', 'name', 'address', 'phone', 'email')
        read_only = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        read_only = ('id', 'created_at', 'updated_at')
