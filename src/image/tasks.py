from diary.models import Diary
from image.services import generate_image as service_generate_image
from celery import shared_task


@shared_task()
def image_task(diary: Diary):
    service_generate_image(diary)
