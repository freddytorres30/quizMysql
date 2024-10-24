from rest_framework import serializers
from .models import Clientes, Reservas, Habitaciones, Pagos


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__' 

    def validate_email(self, value):
        if Clientes.objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo ya está en uso.")
        return value

        
class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'

class HabitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitaciones
        fields = '__all__'
        
class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'