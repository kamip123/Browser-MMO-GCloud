from rest_framework import routers
from cityMap.viewsets import CityOwnedViewSet

router = routers.DefaultRouter()
router.register(r'city', CityOwnedViewSet)
