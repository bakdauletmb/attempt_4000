# core/views.py

from rest_framework import viewsets
from .serializers import SportSerializer
from .models import Sport


class SportViewSet(viewsets.ModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()