from django.shortcuts import render

from rest_framework import generics
from .models import Clientes, Reservas, Habitaciones, Pagos
from .serializers import ClientesSerializer, ReservasSerializer, HabitacionesSerializer, PagosSerializer


# metodos Clientes
class ClientesListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
# metodos Reservas
class ReservasListCreate(generics.ListCreateAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
class ReservasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    
# metodos Habitaciones
class HabitacionesListCreate(generics.ListCreateAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer
class HabitacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer
    
# metodos Pagos
class PagosListCreate(generics.ListCreateAPIView):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
class PagosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer