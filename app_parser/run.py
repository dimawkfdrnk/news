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


def get_exchange_rates():
    url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    response = requests.get(url=url).json()
    data = {course_data['Cur_Abbreviation']: course_data for course_data in response}
    data = {key: data[key] for key in data if key == 'EUR' or key == 'RUB' or key == 'USD'}
    models.ExchangeRates.create_rates(data)

