# Generated by Django 5.1.2 on 2024-10-24 21:33

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_clientes_apellido_alter_clientes_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitaciones',
            name='numero_Habitacion',
            field=models.CharField(max_length=50, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='habitaciones',
            name='tipo_Habitacion',
            field=models.CharField(max_length=100, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='metodoPago',
            field=models.CharField(max_length=100, validators=[api.models.validar_sin_espacios]),
        ),
    ]
