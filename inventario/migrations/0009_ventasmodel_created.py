# Generated by Django 3.0.8 on 2020-10-09 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_auto_20201008_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventasmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
