import urllib
import urllib.request as req

request = req.Request("http://www.baidu.com")
response = req.urlopen(request)
print(response.read())
