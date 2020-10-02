from django.db import models
from proveedor.models import ProveedorModel
from simple_history.models import HistoricalRecords


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

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

class VentasModel(models.Model):
    articulo = models.ForeignKey(ArticuloModel, on_delete=models.PROTECT, default=None)
    vendido = models.IntegerField()

    def __str__(self):
        return self.articulo.nombre

    def get_vendido(self):
        return self.vendido

    def get_cantidad(self):
        return self.articulo.cantidad
    
    def update_cantidad(self):
        self.articulo.cantidad = self.articulo.cantidad - self.vendido
        self.articulo.save()


@receiver(pre_save, sender=VentasModel)
def ventas_detail(sender, **kwargs):
    element = kwargs.get('instance', '')
    ids_ventas = [element.id for element in VentasModel.objects.all()]
    number_cantidad = element.get_cantidad()
    number_vendido = element.get_vendido()

    if element.id not in ids_ventas:
        if number_vendido > number_cantidad:
            return 'imposible'
        else:
            print(element.update_cantidad())
    else:
        print('ACTUALIZADO')


pre_save.connect(ventas_detail, receiver)