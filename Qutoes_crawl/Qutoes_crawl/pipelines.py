# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import  pymongo
from scrapy.exceptions import DropItem


class QutoesCrawlPipeline(object):
    def __init__(self):
        self.limit = 50
    def process_item(self, item, spider):
        if item['text']:
            if len(item['text'])>self.limitL:
                item['text']=item['text'][:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem("sss")
class MongoPipeline(object):
    def __init__(self,url,db):
        self.mongo_url = url
        self.mongo_db = db
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

        @classmethod
        def from_crawler(cls,crawler):
            return cls(
                url = crawler.settings.get('MONGO_URL'),
                db = crawler.settings.get('MONGO_DB')
            )

        def open_spider(self,spider):
            self.client = pymongo.MongoClient(self.mongo_url)
            self.db = self.client[self.mongo_db]

        def process_item(self,item,spider):
            name = item.__class__.__name__
            self.db[name].insert(dict(item))
            return item
        def close_item(self,spider):
            self.client.close()
