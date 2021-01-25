from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import CategoriaInvModel, ArticuloModel, VentasModel

class CategoriaInvAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(CategoriaInvModel, CategoriaInvAdmin)



admin.site.register(ArticuloModel, SimpleHistoryAdmin)

class VentasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )

admin.site.register(VentasModel, VentasAdmin)