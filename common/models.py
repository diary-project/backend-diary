from django.db import models


class BaseModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    class Meta:
        # 해당 옵션을 통해, migrate 시, 별도의 테이블이 생성되지 않고 상속된 클래스들에서 위 항목들이 적용 됨
        abstract = True
