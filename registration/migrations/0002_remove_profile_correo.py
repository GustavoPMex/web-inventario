# Generated by Django 3.0.8 on 2020-08-07 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='correo',
        ),
    ]
