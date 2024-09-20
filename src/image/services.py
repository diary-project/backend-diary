from celery import shared_task

from diary.models import Diary


@shared_task
def generate_image(diary: Diary):
    print(diary)


