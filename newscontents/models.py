from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class NewsContent(models.Model):
    reporter = models.ForeignKey(
        to=USER_MODEL,
        on_delete=models.CASCADE,
        related_name='news_contents',
    )
    headline = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.headline
