from django.db import models


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)  # 날짜 자동 업데이트
    updated = models.DateTimeField(auto_now=True)

    # 추상 모델은 데이터베이스에 등록 되지 않는다.
    class Meta:
        abstract = True
