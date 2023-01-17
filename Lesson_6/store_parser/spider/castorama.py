import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
import scrapy
from urllib.parse import urlencode
from scrapy.http import HtmlResponse
from store_parser.items import StoreParserItem
from scrapy.loader import ItemLoader

class CastoramaSpider(scrapy.Spider):
    name = 'castorama'
    allowed_domains = ['castorama.ru']

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = [f"http://castorama.ru/catalogsearch/result/?{urlencode(kwargs.get('url_args'))}"]

    def parse(self, response: HtmlResponse):
        items_links = response.xpath("//a[contains(@class, 'product-card__name')]")
        for link in items_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=StoreParserItem(), response=response)
        loader.add_xpath("name", "//h1[contains(@class, 'product-essential__name')]/text()")
        loader.add_xpath("price_items", "//div[contains(@class, 'add-to-cart__price')]//div[@class='current-price']//span[@class='price']//text()")
        loader.add_xpath("photos", "//img[contains(@class, 'top-slide__img')]/@data-src")
        loader.add_value("url", response.url)

        params_table_xpath = "//div[contains(@class, 'product-block')]//dl[contains(@class, 'specs-table')]"
        loader.add_xpath("params_names", f"{params_table_xpath}/dt/span[contains(@class, 'specs-table__attribute-name')]/text()")
        loader.add_xpath("params_values", f"{params_table_xpath}/dd[contains(@class, 'specs-table__attribute-value ')]/text()")

        yield loader.load_item()
