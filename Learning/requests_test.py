import requests
import json

# r = requests.get("http://cuiqingcai.com")
# print(type(r))
# print(r.status_code)
# print(r.encoding)
# print(r.cookies)

# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

# params = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type' : 'application/json'}
# r = requests.get("http://httpbin.org/get", params = params, headers = headers)
# print(r.url)

# r = requests.get("https://github.com/timeline.json")
# print(r.text)
# print(r.json())


# r = requests.get("https://github.com/timeline.json", stream=True)
# print(r.raw)
# print(r.raw.read(10))

# params = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data = params)
# print(r.text)

# params = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data = json.dumps(params))
# print(r.text)

# files = {'file': open('a.json', 'rb')}
# r = requests.post("http://httpbin.org/post", files = files)
# print(r.text)

# url = 'http://example.com'
# r = requests.get(url)
# print r.cookies
# print r.cookies['example_cookie_name']

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print(r.text)

# requests.get('http://github.com', timeout=0.001)

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# s = requests.Session()
# s.headers.update({'x-test': 'true'})
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(r.text)

# r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# print(r.text)

# r = requests.get('https://github.com', verify=True)
# print (r.text)