from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Premium(models.Model):
    priceOneMonth = models.FloatField()
    priceHalfYear = models.FloatField()
    priceYear = models.FloatField()

class Tranzakcja(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    typeOfPremium = models.IntegerField(default=1)
    buyingDate = models.DateTimeField(default=timezone.now)
