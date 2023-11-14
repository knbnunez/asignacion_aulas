# Generated by Django 4.1.7 on 2023-11-07 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_aula_aula_compartida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Espacio_Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_combinado', models.CharField(max_length=100)),
                ('aula', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.aula')),
            ],
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.espacio_aula'),
        ),
        migrations.AddIndex(
            model_name='espacio_aula',
            index=models.Index(fields=['nombre_combinado'], name='app_espacio_nombre__105aab_idx'),
        ),
    ]