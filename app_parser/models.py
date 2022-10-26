from django.db import models
from .tasks import save_in_base
class News(models.Model):
    title = models.TextField()
    url = models.TextField()

    @classmethod
    def create_news(cls):
        s = save_in_base()
        for i in s:
            cls.objects.create(title=i['title'], url=i['url'])