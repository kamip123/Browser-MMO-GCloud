from rest_framework import viewsets
from .models import CityOwned
from .serializers import CityOwnedSerializer


class CityOwnedViewSet(viewsets.ModelViewSet):
    queryset = CityOwned.objects.all()
    serializer_class = CityOwnedSerializer
