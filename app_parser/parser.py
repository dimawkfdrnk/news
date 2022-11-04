from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


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
        for url in soup:
            image = (soup[url].find('div', attrs={'id': 'post-content-body'}).find('img'))
            if image != None:
                try:
                    image = image['data-src']
                except KeyError:
                    image = image['src']

            article_data.append({
                'title': soup[url].find('h1').text,
                'image': image,
                'text': soup[url].find('div', attrs={'id': 'post-content-body'}).text,
                'url': url
            })

        return article_data


def get_exchange_rates():
    url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    response = requests.get(url=url).json()

    data = {course_data['Cur_Abbreviation']: course_data for course_data in response}
    data = {key: data[key] for key in data if key == 'EUR' or key == 'RUB' or key == 'USD'}
    for key in data:
        print(key, data[key]['Cur_OfficialRate'])
