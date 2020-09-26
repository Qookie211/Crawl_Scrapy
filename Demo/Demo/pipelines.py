# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import pymongo

from itemadapter import ItemAdapter

from Qutoes_crawl.Qutoes_crawl import settings


class DemoPipeline:
    def __init__(self):
        host= settings['']
        print("实例化DemoPipeline")
        self.f = open('itcast_pipeline.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item))
        self.f.write(content)
        print(content)
        return item
    def colse_spider(self,spider):
        print("over")
        self.f.close()