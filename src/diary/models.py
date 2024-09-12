from django.db import models
from common.models import BaseModel
from diary.consts import WEATHER_CHOICES
from user.models import User


# Create your models here.
class Diary(BaseModel):
    date = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True)
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "diary"
        indexes = [
            models.Index(fields=['user', 'date', 'id'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name="unique_user_date_diary")
        ]
