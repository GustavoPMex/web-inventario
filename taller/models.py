from django.db import models
from cliente.models import ClienteModel
from djchoices import ChoiceItem, DjangoChoices
from registration.models import Profile

class EquipoModel(models.Model):

    class Estado(DjangoChoices):
        pendiente = ChoiceItem('pendiente', 'Pendiente')
        terminado = ChoiceItem('terminado', 'Terminado')

    equipo = models.CharField(max_length=200)
    descripcion = models.TextField()
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    personal = models.ForeignKey(Profile, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.pendiente)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['-creacion']

