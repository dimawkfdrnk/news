from urllib.parse import urljoin
from .models import News
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

    def get_data(self):
        data = []
        for url in self.soup:
            received_data = self.soup[url].find('div', class_='tm-articles-list')
            for i in received_data.find_all('article'):
                data.append({
                'title': i.find('h2').text,
                'url': urljoin(url, i.find('a', class_='tm-article-snippet__title-link')['href'])})

        return data


def save_in_base():
    soup = Crawler(URLS).get_soup()
    habr = Pareser(soup)
    data = habr.get_data()
    return data



