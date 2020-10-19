from django.db import models
from proveedor.models import ProveedorModel
from simple_history.models import HistoricalRecords

from django.forms import ValidationError

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
    articulo = models.ForeignKey(ArticuloModel, on_delete=models.CASCADE)
    vendido = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.articulo.nombre

    def get_vendido(self):
        return self.vendido

    def get_cantidad(self):
        return self.articulo.cantidad
    
    def get_requisitos(self):
        if self.vendido <= self.articulo.cantidad:
            return True
        else:
            return False
        

    def update_cantidad(self):
        self.articulo.cantidad = self.articulo.cantidad - self.vendido
        self.articulo.save()
    


            

@receiver(pre_save, sender=VentasModel)
def ventas_detail(sender, **kwargs):
    # Se obtiene la instancia que se está creando
    element = kwargs.get('instance', '')
    # Se obtienen todos los ids de todos los objetos creados en el modelo "VentasModel"
    ids_ventas = [element.id for element in VentasModel.objects.all()]
    # Se llama al metodo get_cantidad, que retornará la cantidad disponible del articulo que se desea
    number_cantidad = element.get_cantidad()
    # Se llama al metodo_getcantidad, que retornará la cantidad de articulos que se venderán
    number_vendido = element.get_vendido()

    # Comprobamos si el llamado es un create, preguntando si su "id" se encuentra en la lista ids_ventas
    if element.id not in ids_ventas:
        # Comprobamos que lo vendido no exceda el stock
        if element.get_requisitos():
            return element.update_cantidad() 


pre_save.connect(ventas_detail, receiver)