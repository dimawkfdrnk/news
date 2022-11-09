from app_parser import models
from .parser import Crawler, Pareser
import requests


URLS = ['https://habr.com/ru/news/top/daily/']

tags = {
    'received_data': {
        'div': 'div',
        'class': 'tm-articles-list',
        'article': 'article'
    },
    'urls_article': {
        'a': 'a',
        'class': 'tm-article-snippet__title-link'
    },
    'image': {
        'div': 'div',
        'id': 'post-content-body',
        'img': 'img',
        'src': 'src',
        'data-src': 'data-src'
    },
    'title': {
        'h1': 'h1'
    },
    'text': {
        'div': 'div',
        'id': 'post-content-body'
    }
}

def save_in_base():
    all_news = models.News.objects.all()
    soup = Crawler().get_soup(URLS)
    habr = Pareser(tags)
    urls_news = habr.get_urls(soup)
    latest_news = [url for url in urls_news if not url in [news.url for news in all_news]]
    article_data = habr.article_data(latest_news)
    for data in article_data:
        models.News.create_news(title=data['title'], image=data['image'], text=data['text'], url=data['url'])


def get_exchange_rates():
    url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    response = requests.get(url=url).json()
    data = {course_data['Cur_Abbreviation']: course_data for course_data in response}
    data = {key: data[key] for key in data if key == 'EUR' or key == 'RUB' or key == 'USD'}
    models.ExchangeRates.create_rates(data)

