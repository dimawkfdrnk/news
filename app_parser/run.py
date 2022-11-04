from app_parser import models
from .parser import Crawler, Pareser
import requests


URLS = ['https://habr.com/ru/news/top/daily/']

def save_in_base():
    a = models.News.objects.all()
    soup = Crawler(URLS).get_soup()
    habr = Pareser(soup)
    urls_article = habr.get_urls()
    z = [i for i in urls_article if not i in [s.url for s in a]]
    article_data = habr.article_data(z)
    for data in article_data:
        models.News.create_news(data['title'], data['image'], data['text'], data['url'])





# from app_parser.run import save_in_base
# save_in_base()
