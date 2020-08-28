from django.db import models
from cliente.models import ClienteModel
from registration.models import Profile
from djchoices import ChoiceItem, DjangoChoices

class ServicioModel(models.Model):
    
    class Estado(DjangoChoices):
        pendiente = ChoiceItem('pendiente', 'Pendiente')
        terminado = ChoiceItem('terminado', 'Terminado')

    cliente = models.ForeignKey(ClienteModel, on_delete=models.PROTECT, default=None)
    descripcion = models.TextField()
    tecnico = models.ForeignKey(Profile, on_delete=models.PROTECT, default=None)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.pendiente)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-creacion']
