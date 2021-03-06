# Generated by Django 3.0.8 on 2020-09-05 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0002_auto_20200731_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaInvModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='HistorialPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ManyToManyField(to='inventario.CategoriaInvModel')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.ProveedorModel')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'abstract': False,
            },
        ),
    ]
