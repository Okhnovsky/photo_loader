from random import randint

from .models import Photo
from .consumers import update_photo

from celery import shared_task


@shared_task
def test_add(id):
    photo = Photo.objects.get(id=id)
    for _ in range(99):
        Photo.objects.create(
            image_name=photo.image_name,
            file=photo.file,
            random_int=randint(1, 1000),
        )
    update_photo()
