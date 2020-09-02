from django.shortcuts import render
from garantia.models import GarantiaModel

def HomeView(request):
    garantias = GarantiaModel.objects.filter(estado='pendiente')

    context = {
        'garantias':garantias,
    }

    return render(request, 'core/home.html', context)