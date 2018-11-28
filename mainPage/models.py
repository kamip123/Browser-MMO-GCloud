from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import alliance.models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Server(models.Model):
    name = models.CharField(max_length=50)
    playerAmount = models.IntegerField()
    speed = models.FloatField(max_length=10)
    multiplicationValue = models.FloatField(max_length=10)
    nextVillageX = models.IntegerField(default=1575)
    nextVillageY = models.IntegerField(default=1175)
    nextVillageId = models.IntegerField(default=1)

    def update_village_pos(self, x, y):
        self.nextVillageX = x
        self.nextVillageY = y

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alliance = models.OneToOneField(alliance.models.Alliance, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    profilePic = models.FileField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
    until_premium = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CityPositions(models.Model):
    villageX = models.IntegerField(default=1575)
    villageY = models.IntegerField(default=1175)

    def __str__(self):
        return self.id

