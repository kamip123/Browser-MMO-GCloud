from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Alliance(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    vice_creator = models.ForeignKey(User, related_name='vice_creator', on_delete=models.CASCADE, null=True, blank=True)
    alliance_logo = models.FileField(null=True, blank=True)
    members = models.ManyToManyField(User)
    alliance_bio = models.TextField(null=True, blank=True)

    def max_members(self):
        if self.members >= 50:
            return False
        else:
            return True

    def __str__(self):
        return str(self.name)


class PostForum(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class Topic(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(PostForum)


class SubForum(models.Model):
    title = models.CharField(max_length=100)
    topics = models.ManyToManyField(Topic)


class Forum(models.Model):
    sub_forums = models.ManyToManyField(SubForum)
    owner = models.ForeignKey(Alliance, on_delete=models.CASCADE)
