from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import CategoriaInvModel, ArticuloModel

class CategoriaInvAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(CategoriaInvModel, CategoriaInvAdmin)



admin.site.register(ArticuloModel, SimpleHistoryAdmin)
