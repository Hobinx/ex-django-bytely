from django.db import models
from shortener.models import BytelyURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, BytelyURL):
            obj, created = self.get_or_create(bytely_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    bytely_url = models.OneToOneField(BytelyURL, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return f'{self.count}'
