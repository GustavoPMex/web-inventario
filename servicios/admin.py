from django.contrib import admin
from .models import ServicioModel

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')

admin.site.register(ServicioModel, ServicioAdmin)