# Generated by Django 4.1.7 on 2023-11-05 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_comision_bh_comision_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comision_bh',
            name='comision_nombre',
        ),
        migrations.AddField(
            model_name='comision_bh',
            name='comision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comision', to_field='nombre'),
        ),
    ]
