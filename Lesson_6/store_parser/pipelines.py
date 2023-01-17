# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient
from transliterate import translit
import hashlib
import string

from my_lib.utils import hash_struct

class StoreParserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.chain_stores

    def process_item(self, item, spider):
        item['price'], item['currency'] = item['price_items']
        item['params'] = dict(zip(item['params_names'], item['params_values']))

        del item['price_items'], item['params_names'], item['params_values']

        item['_id'] = hash_struct(dict(item))
        collection = self.mongobase[spider.name]
        try:
            collection.insert_one(item)
        except DuplicateKeyError:
            print(f"Document with key {item['_id']} already exists.")
        return item

class StorePhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img_url in item['photos']:
                try:
                    yield scrapy.Request(img_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['photos'] = [item_[1] for item_ in results if item_[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        if item and info.spider:
            folder_name = translit(item['name'], reversed=True) \
                .translate({ord(x): None for x in string.punctuation}) \
                .replace(' ', '_')
            return f'{info.spider.name}/{folder_name}/{image_guid}.jpg'

