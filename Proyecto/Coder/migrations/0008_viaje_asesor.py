# Generated by Django 5.0.1 on 2024-01-14 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0007_rename_asesorporlugar_viajeporasesor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Coder.asesor'),
        ),
    ]
