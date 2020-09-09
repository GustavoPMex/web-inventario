from django.db import models
from proveedor.models import ProveedorModel
from simple_history.models import HistoricalRecords

class CategoriaInvModel(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-creacion']


class ArticuloModel(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ManyToManyField(CategoriaInvModel)
    proveedor = models.ForeignKey(ProveedorModel, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
