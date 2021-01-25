from django import template


register = template.Library()

@register.filter
def traslate_status(status_en):
    return {
        'Created':'Creación',
        'Changed':'Modificación',
        'Deleted':'Eliminación'
    }.get(status_en, 'Sin status')
