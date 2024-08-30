from django.db import models
from common.models import BaseModel
from diary.models import Diary


class Tag(BaseModel):
    word = models.CharField(max_length=20)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=False, related_name='tags')

    def __str__(self):
        return self.word
