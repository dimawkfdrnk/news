from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=400)
    image = models.CharField(max_length=1000, null=True)
    text = models.TextField(blank=True)
    url = models.CharField(max_length=200)

    @classmethod
    def create_news(cls, title, image, text, url):
        cls.objects.create(title=title, image=image, text=text, url=url)

    def get_url(self):
        return reverse('news_page', kwargs={'news_id': self.pk})

    @property
    def number_of_comments(self):
        return models.Comments.objects.filter(news=self).count()


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-creation_date',)


class Likes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
