from django.db import models
from common.models import BaseModel
from diary.models import Diary


# Create your models here.
class Image(BaseModel):
    prompt = models.TextField(blank=True)
    url = models.CharField(max_length=1024)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=False, related_name="images")

    def __str__(self):
        return self.url

    @classmethod
    def build(cls, prompt: str, url: str, diary: Diary):
        return cls(prompt=prompt, url=url, diary=diary)

    class Meta:
        db_table = "image"
