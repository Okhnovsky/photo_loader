from celery import shared_task

from photos.consumers import update_photo
from photos.models import Photo


@shared_task
def add(obj_data, number):
    Photo.objects.create(
        image_name=obj_data.get('image_name'),
        file=obj_data.get('file'),
        random_int=number,
    )
    update_photo()
