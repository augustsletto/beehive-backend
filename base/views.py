from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class getProducts(generics.ListAPIView):
    """
    List all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class getProduct(generics.RetrieveAPIView):
    """
    Retrieve a product instance.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
