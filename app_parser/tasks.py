from urllib.parse import urljoin
import  requests
from bs4 import BeautifulSoup


URLS = ['https://habr.com/ru/news/top/daily/']

class Crawler:
    def __init__(self, urls):
        self.urls = urls

    def get_soup(self):
        data = {}
        for url in self.urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            data.update({url: soup})

        return data


class Pareser(Crawler):

    def __init__(self, soup):
        self.soup = soup

    def get_urls(self):
        urls_article = []
        for key in self.soup:
            received_data = self.soup[key].find('div', class_='tm-articles-list')
            for article in received_data.find_all('article'):
                urls_article.append(urljoin(key, article.find('a', class_='tm-article-snippet__title-link')['href']))
        return urls_article

    def article_data(self, urls_article):
        article_data = []
        soup = Crawler(urls_article).get_soup()
        for key in soup:
            article_data.append({
                'title': soup[key].find('h1').text,
                'image': str(soup[key].find('figure')),
                'text': soup[key].find('div', id='post-content-body').text})

        return article_data



# soup = Crawler(URLS).get_soup()
# habr = Pareser(soup)
# data = habr.get_data()
# d = habr.news_data(['https://habr.com/ru/news/t/695364/'])
# print(data)

