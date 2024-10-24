# Generated by Django 5.1.2 on 2024-10-24 19:31

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='apellido',
            field=models.CharField(max_length=100, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.CharField(max_length=100, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha_Registro',
            field=models.DateTimeField(auto_now_add=True, unique=True, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=100, validators=[api.models.validar_sin_espacios]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=20, validators=[api.models.validar_sin_espacios]),
        ),
    ]
