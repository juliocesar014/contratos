from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Contrato

class CustomUsuarioField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username

class ContratoSerializer(serializers.ModelSerializer):
    usuario = CustomUsuarioField(read_only=True)

    class Meta:
        model = Contrato
        fields = ['id', 'nome', 'arquivo', 'usuario', 'data']
