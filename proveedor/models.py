from django.db import models
from phone_field import PhoneField

class ProveedorModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono_uno = PhoneField()
    telefono_dos = PhoneField(blank=True, null=True)
    correo = models.EmailField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        return super(ProveedorModel , self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-creacion']