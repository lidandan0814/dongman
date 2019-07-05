# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongman.items import ManhuaItem

class ManhuaSpider(CrawlSpider):
    name = 'manhua'
    allowed_domains = ['www.hao123.com']
    start_urls = ['https://www.hao123.com/manhua/list/?finish=%E5%B7%B2%E5%AE%8C%E7%BB%93&audience=&area=&cate=&order=&pn=1']

    rules = (
        Rule(LinkExtractor(allow='http://www.hao123.com/manhua/detail/.*', restrict_css='.item-1 a'), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_css='.next-btn'))
    )

    def parse_item(self, response):
        item = ManhuaItem()
        item['漫画名'] = response.css('.info-wrap .title-wrap::text').extract_first()
        item['作者'] = response.css('.info-list .item:nth-child(1) span:nth-child(2)::text').extract_first()
        item['评分'] = response.css('.word.score::text').extract_first()
        item['地域'] = response.css('.info-list .item:nth-child(2) span:nth-child(2)::text').extract_first()[0:2]
        item['类型'] = response.css('.info-list .item:nth-child(4) span:nth-child(2) a::text').extract_first()
        item['题材'] = response.css('.info-list .item:nth-child(5) span:nth-child(2) a::text').extract_first()
        item['收藏数'] = response.css('.info-list .item:nth-child(3) span:nth-child(2)::text').extract_first()
        item['人气'] = response.css('.info-list .item:nth-child(6) span:nth-child(2)::text').extract_first()
        item['内容简介'] = response.css('.des::text').extract_first()
        yield item
