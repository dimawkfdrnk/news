from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class Crawler:
    def get_soup(self, urls):
        data = {}
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            data.update({url: soup})

        return data


class Pareser(Crawler):

    def __init__(self, tags):
        self.tags = tags

    def get_urls(self, soup):
        urls_article = []

        for key in soup:
            received_data = soup[key].find(self.tags['received_data']['div'],
                                           attrs={'class': self.tags['received_data']['class']})
            received_data = received_data.find_all(self.tags['received_data']['article'])

            for article in received_data:
                urls_article.append(
                    urljoin(key, article.find(self.tags['urls_article']['a'],
                                              attrs={'class': self.tags['urls_article']['class']})['href']))
        return urls_article

    def article_data(self, urls_article):
        article_data = []
        soup = Crawler().get_soup(urls_article)
        for url in soup:
            image = (soup[url].find(self.tags['image']['div'],
                                    attrs={'id': self.tags['image']['id']}).find(self.tags['image']['img']))
            if image != None:
                try:
                    image = image[self.tags['image']['data-src']]
                except KeyError:
                    image = image[self.tags['image']['src']]
            title = soup[url].find(self.tags['title']['h1']).text
            text = soup[url].find(self.tags['text']['div'], attrs={'id': self.tags['text']['id']}).text
            article_data.append({
                'title': title,
                'image': image,
                'text': text,
                'url': url
            })

        return article_data






