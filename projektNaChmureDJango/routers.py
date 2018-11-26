from rest_framework import routers
from cityMap.viewsets import CityOwnedViewSet, HousingViewSet, FarmsViewSet, PowerPlantViewSet, MinesViewSet
from cityMap.viewsets import HInfantryViewSet, InfantryViewSet, LTanksViewSet, HTanksViewSet, MotorizedViewSet
from cityMap.viewsets import PlanesViewSet, BarracksViewSet, TownHallViewSet, RoadsViewSet


router = routers.DefaultRouter()
router.register(r'city', CityOwnedViewSet)
router.register(r'housing', HousingViewSet)
router.register(r'farms', FarmsViewSet)
router.register(r'powerPlant', PowerPlantViewSet)
router.register(r'mines', MinesViewSet)
router.register(r'hInfantry', HInfantryViewSet)
router.register(r'infantry', InfantryViewSet)
router.register(r'lTanks', LTanksViewSet)
router.register(r'hTanks', HTanksViewSet)
router.register(r'motorized', MotorizedViewSet)
router.register(r'planes', PlanesViewSet)
router.register(r'barracks', BarracksViewSet)
router.register(r'townHall', TownHallViewSet)
router.register(r'roads', RoadsViewSet)