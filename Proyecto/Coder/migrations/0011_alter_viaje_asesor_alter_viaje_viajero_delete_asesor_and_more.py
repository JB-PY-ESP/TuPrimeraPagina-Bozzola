# Generated by Django 5.0.1 on 2024-01-28 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0010_alter_viaje_viajero'),
        ('asesor', '0002_alter_asesor_options'),
        ('viajero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asesor.asesor'),
        ),
        migrations.AlterField(
            model_name='viaje',
            name='viajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='viajero.viajero'),
        ),
        migrations.DeleteModel(
            name='Asesor',
        ),
        migrations.DeleteModel(
            name='Viajero',
        ),
    ]
