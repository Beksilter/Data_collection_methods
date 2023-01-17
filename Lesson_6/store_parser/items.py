# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Compose, MapCompose, TakeFirst
import string

def treat_price_items(value):
    value = value.translate({ord(x): None for x in string.whitespace})
    return int(value) if value.isdigit() else value


class StoreParserItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price_items = scrapy.Field(input_processor=MapCompose(treat_price_items))
    price = scrapy.Field()
    currency = scrapy.Field()
    photos = scrapy.Field()
    params_names = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    params_values = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    params = scrapy.Field()
    _id = scrapy.Field()
