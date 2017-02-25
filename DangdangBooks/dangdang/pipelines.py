# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
for items import DangdangItem

class DangdangPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        da_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host = host, port = port)
        tdb = client[db_name]
        self.post = tdb[settings['MONGO_DOCNAME']]

    def process_item(self, item, spider):
        if isinstance(item, DangdangItem):
            try:
                bookInfo = dict(item)
                if self.post.insert(bookInfo)
                    print('fuck')
            except Exception:
                pass

        return item
