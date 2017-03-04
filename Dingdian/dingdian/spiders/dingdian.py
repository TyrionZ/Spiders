import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from dingdian.items import DingdianItem

class MySpider(scrapy.Spider):
    name = 'dingdian'
    allow_domains = ['23wx.com'] 
    # 如果声明则只允许跟进存在于allow_domains中的url
    base_url = 'http://www.23us.com/class/'

    def start_requests(self):
	    for i in range(1, 11):
	        url = self.base_url + str(i) + '_1.html'
	        yield Request(url, self.parse)

    def parse(self, response):
        page_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        base_url = str(response.url)[:-7]
        for i in range(int(page_num)):
            url = base_url + '_' + str(i + 1) + '.html'
            yield Request(url, callback = self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novel_name = td.find('a').get_text()
            novel_url = td.find('a')['href']
            yield Request(novel_url, callback = self.get_chapter, meta = {'name': novel_name, 'url': novel_url})
            # meta是scrapy中传递额外数据的方法
            
    def get_chapter(self, response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novel_url'] = response.meta['url']
        item['category'] = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text().replace('/', '')
        item['author'] = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text().replace('/', '')
        base_url = BeautifulSoup(response.text, 'lxml').find('p', class_ = 'btnlinks').find('a', class_ = 'read')['href']
        item['name_id'] = str(base_url)[:-6:-1].replace('/', '')
        return item

        
		
