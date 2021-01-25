from django.contrib import admin
from .models import GarantiaModel

class GarantiaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(GarantiaModel, GarantiaAdmin)