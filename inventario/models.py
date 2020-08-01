from django.db import models


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
    nombre = models.CharField(max_length=50)
    categoria = models.ManyToManyField(CategoriaInvModel)
    proveedor = models.ManyToOneRel()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.IntegerField()
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
