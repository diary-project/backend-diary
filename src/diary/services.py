from django.db.models import Q, QuerySet
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from diary.exceptions import DiaryNotFoundException
from diary.models import Diary
from user.models import User
from utils.date_utils import DateUtil


def get_diary(user_id: str, date: str) -> Diary:
    try:
        return Diary.objects.get(user_id=user_id, date=date)
    except ObjectDoesNotExist:
        raise DiaryNotFoundException()
    except MultipleObjectsReturned:
        raise


def get_diaries(user_id: str, date: str) -> QuerySet[Diary]:
    return Diary.objects.filter(Q(user_id=user_id) & Q(date=date))


def get_diary_date_by_year_month(user_id: str, year: int, month: int) -> QuerySet[Diary]:
    return Diary.objects.filter(Q(user_id=user_id) & Q(date__year=year) & Q(date__month=month))


def create_diary(user: User, content: str, weather: str) -> Diary:
    today = DateUtil.get_today()
    created_diary = Diary.objects.create(user=user, content=content, weather=weather, date=today)

    # from tag.services import extract_tags_from_diary_content
    # from image.services import generate_image

    # extract_tags_from_diary_content(diary=created_diary)
    # generate_image(diary=created_diary)

    # tag_task.delay(created_diary)

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


# =============== DEVELOP FUCTION ==============================================================================
def create_diary_dev(user_id: str, content: str, weather: str, date: str) -> Diary:
    created_diary = Diary.objects.create(user_id=user_id, content=content, weather=weather, date=date)
    return created_diary
