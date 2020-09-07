from django.contrib import admin
from .models import CategoriaInvModel, ArticuloModel

class CategoriaInvAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(CategoriaInvModel, CategoriaInvAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(ArticuloModel, ArticuloAdmin)