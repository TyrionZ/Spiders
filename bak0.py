import scrapy
from scrapy.selector import Selector
import urllib.request
import re
import json

class doubanSpider(scrapy.Spider):
    name = 'douban'
    

    def start_requests(self):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
        headers = {'User-Agent': user_agent}
        urls = []
        for i in range(1,14):
            url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(i*20)
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, method='GET', callback=self.parse)

    def parse(self, response):
        # hxs = response.body.decode('utf-8')
        print(response.body)
        # hxs = Selector(text=response.body.decode('utf-8'))    # 这句有问题
        # print(hxs)
        # hjson = json.loads(hxs)    # 字典
        # for lis in hjson['subjects']:
	#    filename = lis["title"] + '_' + lis["rate"] + '分' + '.jpg'
        #    urllib.request.urlretrieve(lis["cover"], filename)