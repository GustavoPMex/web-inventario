from django.shortcuts import render
from garantia.models import GarantiaModel
from taller.models import EquipoModel
from servicios.models import ServicioModel

def HomeView(request):
    garantias = GarantiaModel.objects.filter(estado='pendiente')
    equipos = EquipoModel.objects.filter(estado='pendiente')
    servicios = ServicioModel.objects.filter(estado='pendiente')

    context = {
        'garantias':garantias,
        'equipos':equipos,
        'servicios':servicios
    }

    return render(request, 'core/home.html', context)