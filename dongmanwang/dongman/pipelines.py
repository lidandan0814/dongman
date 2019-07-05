# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from openpyxl import Workbook


class OpenpyxlPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.worksheet = self.workbook.create_sheet("dongman")
        self.worksheet.append(['漫画名','作者', '评分', '地域', '类型','题材', '收藏数', '人气', '内容简介'])

    def process_item(self, item, spider):
        line = [item['漫画名'], item['作者'], item['评分'], item['地域'],
            item['类型'], item['题材'], item['收藏数'], item['人气'],item['内容简介']]
        self.worksheet.append(line)
        self.workbook.save('dongman.xlsx')
        return item



class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db,collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection = collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'), collection=crawler.settings.get('COLLECTION'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[self.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
