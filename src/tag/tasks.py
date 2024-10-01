from ai.ai_service import OpenAIService
from diary.models import Diary
from tag.services import extract_tags_from_diary_content
from image.tasks import image_task
from celery import shared_task


@shared_task()
def tag_task(diary: Diary):
    """
    인공지능을 활용하여 일기에 태그를 추출하고 이미지를 분석하는 작업을 실행합니다.

    Args:
        diary (Diary): Diary 인스턴스
    """
    extract_tags_from_diary_content(diary=diary, ai_service=OpenAIService())
    # image_task.delay(diary)
