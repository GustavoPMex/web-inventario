from django.db import models
from cliente.models import ClienteModel
from model_utils import Choices

class GarantiaModel(models.Model):
    STATUSES = Choices((0,'pendiente', _('pendiente')), (1,'entregado', _('entregado')))

    cliente = models.ManyToManyField(ClienteModel)
    articulo = models.TextField()
    tecnico = models.CharField(max_length=100)
    estado = models.IntegerField(choices=STATUSES, default=STATUSES.draft)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre
    
    class Meta:
        verbose_name = 'Garantia'
        verbose_name_plural = 'Garantias'
        ordering = ['-creacion']

