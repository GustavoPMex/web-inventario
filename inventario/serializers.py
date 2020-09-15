from rest_framework import serializers
from .models import CategoriaInvModel

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaInvModel
        fields = ['id', 'nombre']