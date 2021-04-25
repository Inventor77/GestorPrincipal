from guias.models import Guias
from rest_framework import viewsets, permissions
from .serializers import GuiasSerializer

# Guias Viewset


class GuiasViewSet(viewsets.ModelViewSet):
    queryset = Guias.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GuiasSerializer
