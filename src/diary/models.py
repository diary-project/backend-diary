from django.db import models
from django.utils import timezone
from common.models import BaseModel
from user.models import User


# Create your models here.
class Diary(BaseModel):
    WEATHER_CHOICES = [
        ('sunny', '맑음'),
        ('cloudy', '구름'),
        ('rainy', '비'),
        ('snowy', '눈'),
    ]

    date = models.DateField(primary_key=True, auto_now_add=True)
    content = models.TextField(blank=True)
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "diary"
        indexes = [
            models.Index(fields=['user', 'date'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'])
        ]
