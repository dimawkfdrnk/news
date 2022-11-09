from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .run import save_in_base, get_exchange_rates


class News(models.Model):
    title = models.CharField(max_length=400, verbose_name="Заголовок")
    image = models.CharField(max_length=1000, null=True, verbose_name="Ссылка на изображение")
    text = models.TextField(blank=True, verbose_name="Текст новости")
    url = models.CharField(max_length=200, verbose_name="url исходной страницы")
    creation_date_news = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-creation_date_news',)

    @classmethod
    def create_news(cls, title, image, text, url):
        cls.objects.create(title=title, image=image, text=text, url=url)

    @classmethod
    def update_news(cls):
        save_in_base()

    @property
    def get_comments_news(self):
        commens_news = Comments.objects.filter(news=self)
        return commens_news

    @property
    def get_likes_news(self):
        amount = Likes.objects.filter(news=self)
        return amount

    def get_url(self):
        return reverse('news_page', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    comment_text = models.TextField(verbose_name="Текст комментария")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-creation_date',)

    @property
    def delete_comments(self):
        return reverse('news_page', kwargs={'news_id': self.pk})


class Likes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)


class ExchangeRates(models.Model):
    rates = models.JSONField()
    creation_date_rates = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('creation_date_rates',)

    @classmethod
    def create_rates(cls, rates):
        cls.objects.create(rates=rates)

    @classmethod
    def get_rates(cls):
        rates = cls.objects.order_by('creation_date_rates').last()
        return rates

    @classmethod
    def update_rates(cls):
        get_exchange_rates()


class AuthorsArticles(models.Model):
    title = models.CharField(max_length=200, verbose_name="Статья")
    text_article = models.TextField(verbose_name="Текст статьи")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    moderation_done = models.BooleanField(default=False, verbose_name="Модерация выполнена")

    class Meta:
        ordering = ('creation_date',)
        verbose_name = 'Авторская статья'
        verbose_name_plural = 'Авторские статьи'

    @classmethod
    def create_authors_article(cls, **kwargs):
        cls.objects.create(author=kwargs['author'], title=kwargs['title'], text_article=kwargs['text_article'])

    @classmethod
    def get_authors_article(cls):
        articles = AuthorsArticles.objects.filter(moderation_done=True).reverse()[:5]
        return articles

    def __str__(self):
        return self.title