from rest_framework import viewsets, mixins
from core.models import Category, Provider, Product
from . import serializers


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return self.queryset.filter(pk=None)


