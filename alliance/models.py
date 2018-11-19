from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Alliance(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    vicecreator = models.ForeignKey(User, related_name='vicecreator', on_delete=models.CASCADE, null=True, blank=True)
    vicevicecreator = models.ForeignKey(User, related_name='vicevicecreator', on_delete=models.CASCADE, null=True, blank=True)
    allianceLogo = models.FileField(null=True, blank=True)
    members = models.ManyToManyField(User)

    def maxMembers(self):
        if self.members >= 50:
            return False
        else:
            return True

    def __str__(self):
        return str(self.name)
