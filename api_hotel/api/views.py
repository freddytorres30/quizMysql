from django.shortcuts import render

from rest_framework import generics
from .models import Producto,Cliente,Categoria
from .serializers import ProductoSerializer,ClienteSerializer,CategoriaSerializer

# metodos productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer