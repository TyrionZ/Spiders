import scrapy
import requests
from scrapy import Selector
from lxml import etree
from ..items import DangdangItem
from scrapy_redis.spiders import RedisSpider

class DangdangSpider(RedisSpider):
    name = 'dangdangspider'
    redis_key = 'dangdangspider.urls'
    allowed_domains = ['dangdang.com']
    startUrls = 'http://category.dangdang.com/cp01.00.00.00.00.00.html'

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
        yield scrapy.Request(url = self.start_urls, headers = header, method = 'GET', callback = self.parse)

    def parse(self, response):
        lists = response.body.decode('gdk')
        selector = etree.HTML(lists)
        categoriesList = selector.xpath('//*[@id="leftCate"]/ul/li') # XPath查询语言
        for category in categoriesList:
            try:
                category_big = category.xpath('a/text()').pop().replace('  ', '') #大类
                category_big_id = 
                

                