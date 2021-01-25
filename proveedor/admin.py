from django.contrib import admin
from .models import ProveedorModel

class ProveedorAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(ProveedorModel, ProveedorAdmin)