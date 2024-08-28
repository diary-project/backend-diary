from django.db import models
from common.models import BaseModel


# Create your models here.
class Diary(BaseModel):
    content = models.TextField(blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
