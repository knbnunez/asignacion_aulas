# Generated by Django 4.2.6 on 2023-11-14 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_aula_asignacion_espacio_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='espacio_aula',
            name='capacidad_total',
            field=models.IntegerField(null=True),
        ),
    ]
