
import re
from django.core.exceptions import ValidationError
from django.db import models

def validar_sin_espacios(value):
    if not value.strip():
        raise ValidationError('El campo no puede estar vacío o contener solo espacios.')

class Clientes(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_sin_espacios])
    apellido = models.CharField(max_length=100, validators=[validar_sin_espacios])
    email = models.CharField(max_length=100, validators=[validar_sin_espacios])
    telefono = models.CharField(max_length=20, validators=[validar_sin_espacios])
    fecha_Registro = models.DateTimeField(auto_now_add=True, unique=True, validators=[validar_sin_espacios])

    def clean(self):
        # Validar que el correo no esté vacío o solo contenga espacios
        if not self.email or self.email.isspace():
            raise ValidationError('El correo no puede estar vacío.')
        # Validar que el correo contenga solo caracteres válidos
        if not re.match(r'^[\w.-]+@[\w.-]+\.\w+$', self.email): 
            raise ValidationError('El correo contiene caracteres no válidos.')

    def save(self, *args, **kwargs):
        self.clean()
        # Validar que el correo no exista
        if Clientes.objects.filter(email=self.email).exists():
            raise ValidationError('El correo ya está en uso.')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre




class Reservas(models.Model):
    fecha_Entrada = models.DateField()
    cantidad_Noches = models.IntegerField()
    fecha_Reserva = models.DateField(auto_now_add=True)
    Clientes = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    Habitaciones = models.ForeignKey('Habitaciones', on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha_Entrada, self.Clientes, self.Habitaciones
    


class Habitaciones(models.Model):
    numero_Habitacion = models.CharField(max_length=50)
    tipo_Habitacion = models.CharField(max_length=100)
    precioPorNoche  = models.IntegerField()

    def __str__(self):
        return self.numero_Habitacion
    


class Pagos(models.Model):
    monto = models.IntegerField()
    metodoPago = models.CharField(max_length=100)
    fechaPago = models.DateField()
    Reservas = models.ForeignKey('Reservas', on_delete=models.CASCADE)


    def __str__(self):
        return self.monto, self.Reservas
    