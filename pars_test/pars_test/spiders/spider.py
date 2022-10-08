import scrapy
import sqlite3

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['spider.com']
    start_urls = ['http://spider.com/']

    def parse(self, response):
        pass
