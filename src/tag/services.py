from celery import shared_task

from diary.models import Diary
from image.services import generate_image


@shared_task
def generate_tags(diary: Diary):
    print(diary)
    generate_image.delay()



