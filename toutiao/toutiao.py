# params
keyword = '美景'
myDir = 'pics/'

import re
import json
import time
import random

from pathlib import Path
from urllib import error
from urllib import request
from datetime import datetime
from http.client import IncompleteRead
from socket import timeout as socket_timeout
from bs4 import BeautifulSoup
from urllib import parse
from pprint import pprint

# 获取时间戳
def getTimestamp():
    timestamp = str(datetime.timestamp(datetime.today()))
    return timestamp.replace('.', '')[:-3]

def createDir(name):
    directory = Path(name)
    if not directory.exists():
        directory.mkdir()
    return directory

def getArticleUrls(url, headers = None, timeout = 10):
    req = request.Request(url, headers = headers)
    with request.urlopen(req, timeout = timeout) as res:
        d = json.loads(res.read().decode()).get('data')
        if d is None:
            print("数据请求完毕。")
            return 
        
        urls = [x.get('article_url') for x in d if x.get('article_url')]
        return urls

def getPhotoUrls(url, headers = None, timeout = 10):
    req = request.Request(url, headers = headers)
    with request.urlopen(req, timeout = timeout) as res:
        try:
            soup = BeautifulSoup(res.read().decode(errors = 'ignore'), 'html.parser')
            article = soup.find('div', id = 'article-main')
        except:
            return 
        
        if not article:
            print("无法定位到文章主题。")
            return

        heading = article.h1.string

        if keyword not in heading:
            return
        
        imgList = [img.get('src') for img in article.find_all('img') if img.get('src')]
        return heading, imgList

def save(url, sdir, timeout = 10):
    print(url)
    name = url.rsplit('/', 1)[-1] + '.jpg'
    path = sdir / name

    with request.urlopen(url, timeout = timeout) as res, path.open('wb') as f:
        f.write(res.read())
        print('已下载图片: {sdir}/{name}, 请求的URL为：{url}'
                .format(sdir = sdir, name = name, url = url))

if __name__ == '__main__':
    offset = 0 # 请求的偏移量
    sdir = createDir(myDir) 
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    }

    while True:
        timestamp = getTimestamp()
        params = {
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': 20,
            '_': timestamp
        }
        queryUrl = 'http://www.toutiao.com/search_content/?' + parse.urlencode(params) #将查询参数编码为url

        articleUrls = getArticleUrls(queryUrl, request_headers)
        
        if articleUrls is None:
            break
        
        for x in articleUrls:
            try:
                photoUrls = getPhotoUrls(x, request_headers)

                if photoUrls is None:
                    continue

                heading, photoUrls = photoUrls

                tdir = createDir(sdir / heading)

                for p in photoUrls:
                    try:
                        save(p, tdir)
                    except IncompleteRead as e:
                        print(e)
                        continue
            except socket_timeout:
                print("连接超时。")
                time.sleep(random.randint(15, 25))
                continue
            except error.HTTPError:
                continue

        offset += 20




