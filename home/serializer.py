from rest_framework import serializers
from .models import ramo_atividade


class RamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ramo_atividade