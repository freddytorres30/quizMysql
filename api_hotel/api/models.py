from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_Registro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nombre



class Reservas(models.Model):
    fecha_Entrada = models.DateField()
    cantidad_Noches = models.IntegerField()
    fecha_Reserva = models.DateField(auto_now_add=True)
    Clientes = models.ForeignKey('Clientes', on_delete=models.CASCADE,)
    Habitaciones = models.ForeignKey('Habitaciones', on_delete=models.CASCADE,)

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
    Reservas = models.ForeignKey('Reservas', on_delete=models.CASCADE, related_name='Pagos')


    def __str__(self):
        return self.monto, self.Reservas
    