# Generated by Django 5.0.1 on 2024-01-14 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('id_asesor', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Coder.asesor'),
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
