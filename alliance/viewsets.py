from rest_framework import viewsets
from .models import Alliance
from .serializers import AllianceSerializer


class AllianceViewSet(viewsets.ModelViewSet):
    queryset = Alliance.objects.all()
    serializer_class = AllianceSerializer

















