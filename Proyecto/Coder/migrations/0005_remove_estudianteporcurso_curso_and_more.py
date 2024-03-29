# Generated by Django 5.0.1 on 2024-01-14 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0004_viajero_alter_estudianteporcurso_estudiante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudianteporcurso',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='estudianteporcurso',
            name='estudiante',
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('viajero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Coder.viajero')),
            ],
        ),
        migrations.CreateModel(
            name='AsesorPorLugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coder.asesor')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coder.viaje')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='EstudiantePorCurso',
        ),
    ]
