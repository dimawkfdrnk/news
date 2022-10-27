from django.db import models

class News(models.Model):
    title = models.CharField(max_length=400)
    image = models.TextField()
    text = models.TextField()

    @classmethod
    def create_news(cls, title, image, text):
        cls.objects.create(title=title, image=image, text=text)