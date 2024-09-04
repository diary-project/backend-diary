from django.db import models
from django.utils import timezone
from common.models import BaseModel
from user.models import User


# Create your models here.
class Diary(BaseModel):
    date = models.DateField(primary_key=True, default=timezone.now)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "diary"
