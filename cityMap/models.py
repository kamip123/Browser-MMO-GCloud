from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

# Create your models here.


class CityOwned(models.Model):
    # techniczne
    cityOwner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cityName = models.CharField(max_length=100, default="City")
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

    #def changeToGhostCity(self):
    #    self.cityOwner = 0

    infantry = models.IntegerField(default=0)
    hinfantry = models.IntegerField(default=0)
    planes = models.IntegerField(default=0)
    ltanks = models.IntegerField(default=0)
    htanks = models.IntegerField(default=0)
    motorized = models.IntegerField(default=0)

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
