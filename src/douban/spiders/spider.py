# -*- coding: utf-8 -*-
#from scrapy.contrib.spiders import CrawlSpider
from scrapy.spiders import CrawlSpider

class Douban(CrawlSpider):
    name = "douban"
    start_urls = ['http://www.baidu.com']
    def parse(self,response):
        print response.body
        print response.url
