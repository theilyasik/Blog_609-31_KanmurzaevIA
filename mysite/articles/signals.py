from django.dispatch import receiver
from django.db.models import signals
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from .models import Article

@receiver(signals.pre_save, sender=Article)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        random_part = get_random_string(6)
        base = instance.title or 'article'
        instance.slug = slugify(f"{base}-{random_part}")

