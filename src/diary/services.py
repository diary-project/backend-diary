from typing import List

from django.conf import settings
from django.core.cache import cache
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from ai.ai_service import FakeAIService
from diary.exceptions import DiaryNotFoundException
from diary.models import Diary
from user.models import User
from utils.date_utils import DateUtil


def get_diary(user_id: str, date: str) -> Diary:
    cache_key = f"diary:{user_id}:{date}"
    diary = cache.get(cache_key)

    if diary:
        return diary

    try:
        diary = Diary.objects.get(user_id=user_id, date=date)
        cache.set(cache_key, diary, timeout=settings.CACHE_TIMEOUT)  # 캐시에 저장
        return diary
    except ObjectDoesNotExist:
        raise DiaryNotFoundException()
    except MultipleObjectsReturned:
        raise


def get_diary_date_list_by_year_month(user_id: str, year: int, month: int) -> List[str]:
    cache_key = f"diaries:{user_id}:{year}:{month}"

    # 캐시에서 데이터 가져오기
    diary_date_list = cache.get(cache_key)

    if diary_date_list is not None:
        return diary_date_list

    diary_queryset = Diary.objects.filter(Q(user_id=user_id) & Q(date__year=year) & Q(date__month=month))
    diary_date_list = list(diary_queryset.values_list("date", flat=True))
    cache.set(cache_key, diary_date_list, timeout=settings.CACHE_TIMEOUT)

    return diary_date_list


def create_diary(user: User, content: str, weather: str, date: str = None) -> Diary:
    if not date:
        date = DateUtil.get_today()
    created_diary = Diary.objects.create(user=user, content=content, weather=weather, date=date)

    (year, month, _) = date.split("-")
    cache_key = f"diaries:{user.id}:{year}:{month}"
    cache.delete(cache_key)

    fake_create_tags_and_image(created_diary)

    return created_diary


def update_diary(user: User, date: str, content: str = None, weather: str = None) -> Diary:
    diary = get_diary(user_id=user.id, date=date)
    update_fields = _get_update_fields(content=content, weather=weather)

    if update_fields:
        for field, value in update_fields.items():
            setattr(diary, field, value)
        diary.save()

    return diary


def _get_update_fields(**fields):
    return {key: value for key, value in fields.items() if value is not None}


def delete_diary(user: User, date: str) -> None:
    diary = get_diary(user_id=user.id, date=date)
    if diary:
        diary.delete()


def fake_create_tags_and_image(created_diary: Diary) -> None:
    from tag.tasks import fake_tag_task

    fake_tag_task(diary=created_diary)


def create_tags_and_image(created_diary: Diary) -> None:
    from tag.tasks import tag_task

    tag_task(diary=created_diary)
