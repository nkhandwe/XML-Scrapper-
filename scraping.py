import requests
from bs4 import BeautifulSoup


def hackernews_rss():
    article_list = []
    return new_func(article_list)


def new_func(article_list):
        r = requests.get('https://news.ycombinator.com/rss')
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
            }
            article_list.append(article)
        return print(article_list)


print('Starting scraping')
hackernews_rss()
print('Finished scraping')
