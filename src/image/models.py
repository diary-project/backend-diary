from django.db import models
from common.models import BaseModel
from diary.models import Diary


# Create your models here.
class Image(BaseModel):
    prompt = models.TextField(blank=True)
    url = models.CharField(max_length=1024)
    diary = models.OneToOneField(Diary, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.url
