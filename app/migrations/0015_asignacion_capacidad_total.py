# Generated by Django 4.2.6 on 2023-11-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_espacio_aula_capacidad_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='capacidad_total',
            field=models.IntegerField(default=0),
        ),
    ]