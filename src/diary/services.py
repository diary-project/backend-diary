from django.db.models import Q, QuerySet
from django.core.exceptions import ObjectDoesNotExist

from diary.exceptions import DiaryNotFoundException
from diary.models import Diary
from user.models import User


def get_diary(user_id: str, date: str) -> Diary:
    try:
        return Diary.objects.get(user_id=user_id, date=date)
    except ObjectDoesNotExist:
        raise DiaryNotFoundException()


def get_diaries(user_id: str, date: str) -> QuerySet[Diary]:
    return Diary.objects.filter(Q(user_id=user_id) & Q(date=date))


def get_diary_date_by_year_month(
    user_id: str, year: int, month: int
) -> QuerySet[Diary]:
    return Diary.objects.filter(
        Q(user_id=user_id) & Q(date__year=year) & Q(date__month=month)
    )


def create_diary(user: User, content: str, weather: str) -> Diary:
    return Diary.objects.create(user=user, content=content, weather=weather)


def update_diary(
    user: User, date: str, content: str = None, weather: str = None
) -> Diary:
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
