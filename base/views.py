from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from .products import products


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/products',
        '/products/create/',

        '/products/upload',

        '/products/<id>/reviews/',

        '/products/top/',
        '/products/<id>/',

        '/products/delete/<id>',
        '/products/<update>/<id>',

        

    ]

    return Response(routes)
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = None
    for i in products:
        if i['_id'] == pk:
            product = i
            break

    return Response(product)