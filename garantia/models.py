from django.db import models
from cliente.models import ClienteModel
from djchoices import ChoiceItem, DjangoChoices

class GarantiaModel(models.Model):
    
    class Estado(DjangoChoices):
        pendiente = ChoiceItem('pendiente', 'Pendiente')
        terminado = ChoiceItem('terminado', 'Terminado')

    cliente = models.ForeignKey(ClienteModel, on_delete=models.PROTECT, default=None)
    articulo = models.TextField()
    tecnico = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.pendiente)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre
    
    class Meta:
        verbose_name = 'Garantia'
        verbose_name_plural = 'Garantias'
        ordering = ['-creacion']

