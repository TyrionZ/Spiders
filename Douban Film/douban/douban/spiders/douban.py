import scrapy
import json
import urllib

class doubanSpider(scrapy.Spider):
    name = 'douban'

    def start_requests(self):
        urls = []
        for i in range(14):
            urls.append('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start' + str(i * 20))
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url = url, headers = headers, method = 'GET', callback = self.parse)

    def parse(self, response):
        table = json.loads(response.body.decode('utf-8'))['subjects']
        for element in table:
            filename = element['title'] + '_' + element['rate'] + '分.jpg'
            urllib.request.urlretrieve(element['cover'], filename)


