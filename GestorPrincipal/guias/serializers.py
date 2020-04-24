from rest_framework import serializers
from guias.models import Guias

# Guias Serializer


class GuiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guias
        fields = '__all__'
