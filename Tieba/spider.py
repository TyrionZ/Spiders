import re
from urllib import request

class clearTool:
	img = re.compile('<img.*?>| {7}')
	addr = re.compile('<a.*?>|</a>')
	line = re.compile('<tr>|<div>|</div>|</p>')
	td = re.compile('<td>')
	para = re.compile('<p.*?>')
	br = re.compile('<br><br>|<br>')
	other = re.compile('<.*?>')

	def clear(self, x):
		x = re.sub(self.img, ' [图片] ', x)
		x = re.sub(self.addr, '', x)
		x = re.sub(self.line, '\n', x)
		x = re.sub(self.td, '\t', x)
		x = re.sub(self.para, '\n\t', x)
		x = re.sub(self.br, '\n', x)
		x = re.sub(self.other, '', x)

		return x.strip()

class TBSpider:
	def __init__(self, base_url, see_lz):
		self.base_url = base_url
		self.see_lz = '?see_lz=' + str(see_lz)

	def get_page(self, page_num):
		try:
			url = self.base_url + self.see_lz + '&pn=' + str(page_num)
			req = request.Request(url)
			response = request.urlopen(req)
			# print(response.read())
			return response
		except Exception as e:
			if hasattr(e, 'reason'):
				print('Fail:', e.reason)
			else:
				print('Fail: Unknown Reason.')
	
	def get_title(self):
		page = self.get_page(1)
		pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>')
		result = re.search(pattern, str(page.read().decode('UTF-8')))
		if result:
			# print(result.group(1))
			return result.group(1).strip() # group(1)代表第一个括号里的内容

	def get_page_number(self):
		page = self.get_page(1)
		pattern = re.compile('<li class="l_reply_num".*?>回复贴，共<span class="red">(.*?)</span>页</li>')
		result = re.search(pattern, str(page.read().decode('UTF-8')))
		if result:
			# print(result.group(1))
			return int(result.group(1).strip())

	def get_page_content(self, page_num):
		page = self.get_page(page_num)
		pattern = re.compile('<div id="post_content_.*?">(.*?)</div>') # 正则表达式要写'.*?'，才会贪心匹配最少
		items = re.findall(pattern, str(page.read().decode('UTF-8')))
		return items
	
	def get_contents(self):
		page_number = self.get_page_number()
		contents = []
		for i in range(page_number):
			contents += self.get_page_content(i + 1)
		return contents
		

print('请输入帖子代号：')
base_url = 'http://tieba.baidu.com/p/' +str(input(u'http://tieba.baidu.com/p/'))
see_lz = input("是否只获取楼主发言，是输入1，否输入0\n")
spider = TBSpider(base_url, see_lz)

title = spider.get_title()
file = open(title, 'w')
contents = spider.get_contents()
tool = clearTool()
for item in contents:
	print("------------------------------------------------------------------------------------------------------------------------------------\n" + tool.clear(item), file = file)

