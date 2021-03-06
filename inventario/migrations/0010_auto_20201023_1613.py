# Generated by Django 3.0.8 on 2020-10-23 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20200731_2009'),
        ('inventario', '0009_ventasmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulomodel',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.ProveedorModel'),
        ),
        migrations.AlterField(
            model_name='ventasmodel',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ArticuloModel'),
        ),
    ]
