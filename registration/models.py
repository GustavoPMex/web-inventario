from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User


class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    direccion = models.TextField()
    telefono = PhoneField()

    def __str__(self):
            return str(self.usuario)

    def save(self, *args, **kwargs):
        self.usuario = self.usuario.title() 
        return super(Profile, self).save(*args, **kwargs)