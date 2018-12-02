from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
