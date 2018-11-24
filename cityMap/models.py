from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class Barracks(models.Model):
    productionSpeed = models.IntegerField(default=1)
    pointsPerLvl = models.IntegerField(default=5)


class TownHall(models.Model):
    productionSpeed = models.IntegerField(default=1)
    lvlToUnlockPlanes = models.IntegerField(default=25)
    lvlToUnlockHtanks = models.IntegerField(default=20)
    lvlToUnlockLtanks = models.IntegerField(default=15)
    lvlToUnlockMotorized = models.IntegerField(default=10)
    lvlToUnlockHinfantry = models.IntegerField(default=5)
    pointsPerLvl = models.IntegerField(default=10)


class Roads(models.Model):
    productionSpeed = models.IntegerField(default=1)
    pointsPerLvl = models.IntegerField(default=3)


class Mines(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)


class PowerPlant(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)


class Farms(models.Model):
    resourceProduction = models.IntegerField(default=10)
    pointsPerLvl = models.IntegerField(default=2)


class Housing(models.Model):
    population = models.IntegerField(default=100)
    pointsPerLvl = models.IntegerField(default=1)

class Infantry(models.Model):
    hp = models.IntegerField(default=10)
    attack = models.IntegerField(default=10)
    speed = models.IntegerField(default=20)
    capacity = models.IntegerField(default=30)


class HInfantry(models.Model):
    hp = models.IntegerField(default=30)
    attack = models.IntegerField(default=30)
    speed = models.IntegerField(default=10)
    capacity = models.IntegerField(default=10)


class LTanks(models.Model):
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=100)
    speed = models.IntegerField(default=80)
    capacity = models.IntegerField(default=100)


class HTanks(models.Model):
    hp = models.IntegerField(default=200)
    attack = models.IntegerField(default=100)
    speed = models.IntegerField(default=30)
    capacity = models.IntegerField(default=150)


class Motorized(models.Model):
    hp = models.IntegerField(default=50)
    attack = models.IntegerField(default=50)
    speed = models.IntegerField(default=100)
    capacity = models.IntegerField(default=250)


class Planes(models.Model):
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=200)
    speed = models.IntegerField(default=300)
    capacity = models.IntegerField(default=150)


class CityOwned(models.Model):
    # techniczne
    cityOwner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cityName = models.CharField(max_length=100, default="City")
    is_capital = models.BooleanField(default=False)
    pozX = models.IntegerField(default=1)
    pozY = models.IntegerField(default=1)
    # budynki
    ratusz = models.IntegerField(default=1)
    ratuszBudowa = models.DateTimeField(blank=True, null=True)
    ratuszBudowaTrwa = models.IntegerField(default=0)

    koszary = models.IntegerField(default=1)
    koszaryBudowa = models.DateTimeField(blank=True, null=True)
    koszaryBudowaTrwa = models.IntegerField(default=0)

    drogi = models.IntegerField(default=1)
    drogiBudowa = models.DateTimeField(blank=True, null=True)
    drogiBudowaTrwa = models.IntegerField(default=0)

    kopalnia = models.IntegerField(default=1)
    kopalniaBudowa = models.DateTimeField(blank=True, null=True)
    kopalniaBudowaTrwa = models.IntegerField(default=0)

    elektrownia = models.IntegerField(default=1)
    elektrowniaBudowa = models.DateTimeField(blank=True, null=True)
    elektrowniaBudowaTrwa = models.IntegerField(default=0)

    farmy = models.IntegerField(default=1)
    farmyBudowa = models.DateTimeField(blank=True, null=True)
    farmyBudowaTrwa = models.IntegerField(default=0)

#    def changeToGhostCity(self):
#        self.cityOwner = 0

    infantry = models.IntegerField(default=0)
    hinfantry = models.IntegerField(default=0)
    planes = models.IntegerField(default=0)
    ltanks = models.IntegerField(default=0)
    htanks = models.IntegerField(default=0)
    motorized = models.IntegerField(default=0)

    infantrySupport = models.IntegerField(default=0)
    hinfantrySupport = models.IntegerField(default=0)
    planesSupport = models.IntegerField(default=0)
    ltanksSupport = models.IntegerField(default=0)
    htanksSupport = models.IntegerField(default=0)
    motorizedSupport = models.IntegerField(default=0)

    food = models.IntegerField(default=0)
    electrity = models.IntegerField(default=0)
    ore = models.IntegerField(default=0)
    population = models.IntegerField(default=100)
    points = models.IntegerField(default=100)

    def updatePoints(self, building):
        self.points += building.pointsPerLvl

    def __str__(self):
        return self.cityName

    def rozbudujRatusz(self):
        self.ratuszBudowaTrwa = 1
        self.ratuszBudowa = datetime.now() + timedelta(seconds=5)

    def updateBuildings(self):
        if self.ratuszBudowaTrwa == 1:
            if timezone.now() > self.ratuszBudowa:
                self.ratuszBudowaTrwa = 0
                self.ratusz += 1
