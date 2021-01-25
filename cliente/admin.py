from django.contrib import admin
from .models import ClienteModel

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'modificacion')


admin.site.register(ClienteModel, ClienteAdmin)
