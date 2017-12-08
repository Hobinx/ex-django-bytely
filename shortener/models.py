from django.conf import settings
from django.db import models
from .utils import create_shortcode


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class BytelyURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(BytelyURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = BytelyURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code += 1
        return f'New codes made: {new_code}'


class BytelyURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=SHORTCODE_MAX, default='abc',
                                 unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = BytelyURLManager()

    def save(self, *args, **kwargs):

        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(BytelyURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
