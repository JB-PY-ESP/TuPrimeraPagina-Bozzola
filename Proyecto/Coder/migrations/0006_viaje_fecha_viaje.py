# Generated by Django 5.0.1 on 2024-01-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0005_remove_estudianteporcurso_curso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='fecha_viaje',
            field=models.DateField(blank=True, null=True),
        ),
    ]
