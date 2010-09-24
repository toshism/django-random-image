import os
import random
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def random_image(image_dir):
    try:
        valid_extensions = settings.RANDOM_IMAGE_EXTENSIONS
    except AttributeError:
        valid_extensions = ['.jpg','.jpeg','.png','.gif',]

    if image_dir:
        rel_dir = image_dir
    else:
        rel_dir = settings.RANDOM_IMAGE_DIR
    rand_dir = os.path.join(settings.MEDIA_ROOT, rel_dir)

    files = [f for f in os.listdir(rand_dir) if os.path.splitext(f)[1] in valid_extensions]

    return os.path.join(rel_dir, random.choice(files))
