from urllib import request
import re

file = open("qiushi.txt", "w")

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
tool = clearTool()

def get_page(page_num):
	url = 'http://www.qiushibaike.com/hot/page/' + str(page_num)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

	try:
		req = request.Request(url, headers = headers)
		response = request.urlopen(req)
		page = response.read().decode('UTF-8')
	except request.URLError as e:
		if hasattr(e, "code"):
			print("Fail:" + str(e.code) + e.reason)
		else:
			print("Fail: Unknown Reason")
		return 
	
	pattern = re.compile('<div class="content">\n*(.*?)\n*</div>')
	contents = re.findall(pattern, page)
	for item in contents:
		img = re.search('img', item)
		if img:
			print('----------------------------------------------------\n'+tool.clear(item), file = file)

for i in range(7):
	get_page(i)
