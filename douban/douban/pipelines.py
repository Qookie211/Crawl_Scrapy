# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sys

from douban import settings

sys.path.append('D:\Scrapy_crawl\douban\douban')
import pymongo



class DoubanPipeline:

    def __init__(self):

        host = settings.MONGODB_DBNAME

        port = settings.MONGODB_PORT

        dbname = settings.MONGODB_DBNAME

        sheetname = settings.MONGODB_SHEETNAME

        # 创建MONGODB数据库链接

        client = pymongo.MongoClient(host=host, port=port)

        # 指定数据库

        mydb = client[dbname]

        # 存放数据的数据库表名

        self.sheet = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)

        self.sheet.insert(data)

        return item

#     def process_item(self, item, spider):
#         content = json.dumps(dict(item))
#         self.f.write(content)
#         print(content)
#         return item
