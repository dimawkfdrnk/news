from app_parser import models
from .tasks import Crawler, Pareser

URLS = ['https://habr.com/ru/news/top/daily/']

def save_in_base():
    soup = Crawler(URLS).get_soup()
    habr = Pareser(soup)
    urls_article = habr.get_urls()
    article_data = habr.article_data(urls_article)
    for data in article_data:
        models.News.create_news(data['title'], data['image'], data['text'])



# def filt(link):
#     a = models.News.objects.filter(url=link)
#     if a:
#         print('YES!')

# from app_parser.run import save
# ['https://habr.com/ru/news/t/695498/']