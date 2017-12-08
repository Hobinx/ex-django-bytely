from django.core.management.base import BaseCommand
from shortener.models import BytelyURL


class Command(BaseCommand):
    help = 'Refresh all BytelyURL short code'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **kwargs):
        return BytelyURL.objects.refresh_shortcodes(items=kwargs['items'])
