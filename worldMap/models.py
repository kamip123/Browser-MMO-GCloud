from django.db import models
from django.utils import timezone
from cityMap.models import CityOwned
from django.db.models.signals import post_save
from django.dispatch import receiver
from background_task import background


class Attack(models.Model):
    attacker = models.ForeignKey(CityOwned, related_name='attackerwm', on_delete=models.CASCADE)
    defender = models.ForeignKey(CityOwned, related_name='defenderwm', on_delete=models.CASCADE)
    arrive = models.DateTimeField(default=timezone.now)
    send = models.DateTimeField(default=timezone.now)


@receiver(post_save, sender=Attack)
def delete_attack_recive(sender, instance, created, **kwargs):
    if created:
        delete_attack(instance.id, schedule=10)


@background(schedule=1)
def delete_attack(id_of_attack):
    Attack.objects.get(id=id_of_attack).delete()


