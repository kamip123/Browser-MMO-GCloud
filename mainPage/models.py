from django.db import models
from django.utils import timezone


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

    def __str__(self):
        return self.name
