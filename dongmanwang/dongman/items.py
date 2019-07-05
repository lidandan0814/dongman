# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ManhuaItem(Item):
    漫画名 = Field()
    作者 = Field()
    评分 = Field()
    地域 = Field()
    类型 = Field()
    题材 = Field()
    收藏数 = Field()
    人气 = Field()
    内容简介 = Field()
    
