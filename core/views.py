from django.shortcuts import render
from garantia.models import GarantiaModel
from taller.models import EquipoModel
from servicios.models import ServicioModel

def HomeView(request):
    garantias = GarantiaModel.objects.filter(estado='pendiente')
    if request.user.is_superuser:
        equipos = EquipoModel.objects.filter(estado='pendiente', personal__usuario=request.user)
        servicios = ServicioModel.objects.filter(estado='pendiente')
    else:
        equipos = EquipoModel.objects.filter(estado='pendiente', personal__usuario=request.user)
        servicios = ServicioModel.objects.filter(estado='pendiente',  tecnico__usuario=request.user)


    context = {
        'garantias':garantias,
        'equipos':equipos,
        'servicios':servicios
    }

    return render(request, 'core/home.html', context)