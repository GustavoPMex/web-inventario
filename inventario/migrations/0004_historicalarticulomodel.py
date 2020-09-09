# Generated by Django 3.0.8 on 2020-09-08 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20200731_2009'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0003_auto_20200907_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalArticuloModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad', models.IntegerField()),
                ('creacion', models.DateTimeField(blank=True, editable=False)),
                ('modificacion', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('proveedor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='proveedor.ProveedorModel')),
            ],
            options={
                'verbose_name': 'historical Articulo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
