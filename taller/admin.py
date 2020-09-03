from django.contrib import admin
from .models import EquipoModel

# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')


admin.site.register(EquipoModel, EquipoAdmin)