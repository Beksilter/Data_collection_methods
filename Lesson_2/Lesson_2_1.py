from pprint import pprint
import requests
from lxml.html import fromstring
from pymongo import MongoClient


class DzenNews:
    def __init__(self):
        self.url = "https://dzen.ru/news/"
        self.headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        self.params = {'issue_tld': 'ru', 'sso_failed': ''}
        self.items_xpath = "//div[contains(@class,'mg-card ')]"

        self.title_xpath = ".//h2/a/text()"
        self.ref_xpath = ".//h2/a/@href"
        self.datetime_xpath = './/span[@class="mg-card-source__time"]/text()'
        self.source_xpath = ".//a[@class='mg-card__source-link']/text()"

    def get_news(self):
        r = requests.get(self.url, headers=self.headers, params=self.params)
        dom = fromstring(r.text)
        items = dom.xpath(self.items_xpath)

        for item in items:
            info = {}
            title = item.xpath(self.title_xpath)[0]
            datetime = item.xpath(self.title_xpath)[0]
            source = 'https://dzen.ru'
            url = self.url + item.xpath(self.ref_xpath)[0]
            info["title"] = title.replace('\xa0', ' ')
            info["url"] = url
            info["datetime"] = datetime
            info["source"] = source
            mongo.save_one_item_with_update(info)





class LentaRuNews:
    def __init__(self):
        self.url = "https://lenta.ru/"
        self.headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

        }
        self.items_xpath = "//div[contains (@class, 'topnews')]//div[contains (@class, 'card-mini__text')]"
        self.title_xpath = ".//text()"
        self.ref_xpath = "./parent::a/@href"
        self.datetime_xpath = './/span[contains (@class, "js-ago")]//@datetime'
        self.source_xpath = './/a[contains (@class, "breadcrumbs__link")]//@href'

    def get_news(self):
        r = requests.get(self.url, headers=self.headers)
        dom = fromstring(r.text)
        items = dom.xpath(self.items_xpath)

        for item in items:
            info = {}
            title = item.xpath(self.title_xpath)[0]
            datetime = item.xpath(self.title_xpath)[1]
            source = 'lenta.ru'
            url = self.url + item.xpath(self.ref_xpath)[0]
            info["title"] = title.replace('\xa0', ' ')
            info["url"] = url
            info["datetime"] = datetime
            info["source"] = source
            mongo.save_one_item_with_update(info)


class MongoMagic:
    def __init__(self):
        self.mongo_host = "localhost"
        self.mongo_port = 27017
        self.mongo_db = "News"
        self.mongo_collection = "News"

    def save_one_item_with_update(self, item):
        with MongoClient(self.mongo_host, self.mongo_port) as client:
            db = client[self.mongo_db]
            collection = db[self.mongo_collection]
            collection.update_one(
                {"url": item["url"]},
                {"$set": {"title": item["title"],
                          "datetime": item["datetime"],
                          "source": item["source"]}
                 },
                upsert=True,
            )


if __name__ == "__main__":
    mongo = MongoMagic()

    dzen = DzenNews()
    dzen.get_news()

    lenta = LentaRuNews()
    lenta.get_news()