from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    direccion = models.TextField()
    telefono = PhoneField()
    correo = models.EmailField()