import Queue, urllib, urllib2, cookielib, socket, json, demjson, time, gevent
from gevent import monkey
monkey.patch_all()
from pathlib import Path

def getPages(x):
        global params
    	url = "http://223.99.170.13:9001/CloudBaseTBC/ajaxDataCollection"

        socket.setdefaulttimeout(40)
	params['pageIndex'] = str(x)
	iHeaders = {"Type": "application/x-www-form-urlencoded; charset=UTF-8",
		    "Cookie": ""}

	req = urllib2.Request(url, headers = iHeaders)

	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, urllib.urlencode(params))
        data = response.read()
	parsed = json.loads(data)
        return parsed

def getTotalPages():
    while True:
        try:
            data = getPages(1)
            break 
        except:
            continue

    total = int(data['page']['totalPages'])
    return total

def crawl(x):
        global current, top, stack, cont
       
        current += 1
        print 'start' + str(x) + ' ' + str(current)
        try:
            data = getPages(x)
            for i in range(0, 20):
		json.dump(data['dataCollection'][i], output)
                print >> output
            print x
            cont = 0
        except:
            stack[top] = x
            top += 1
            print 'error' + str(x)
            cont += 1
        current -= 1
        print 'end' + str(x) + ' ' + str(current)


def apart(sdir):
    global cont, current, total, minNum, bottom, stack, top
    print str(sdir) + 'start...TotalPages is: ' + str(total) + '....'
    output = (sdir / 'data').open('w')
    record = (sdir / 'record').open('w')
    current = 0
    minNum = 0
    bottom = 0
    stack = range(total, bottom, -1)
    top = total - bottom
    number = 18
    cont = 0
    while True:
        time.sleep(.01)
        if (current == 0):
            if (top == 0):
                break 

        if (cont >= 200): 
            print 'cookie?'
            print >> record, minNum
            while (stack[top - 1] < minNum):
                top -= 1
                print stack[top]
                print >> record, stack[top]
            print minNum
            print >> record, 0
            break  
        if (current < number): 
            for i in range(number - current):
                if (top == 0):
                    break
                top -= 1
                if (stack[top] > minNum):
                    minNum = stack[top]
                gevent.spawn(crawl, stack[top])
        
    output.close()
    record.close()

if __name__ == '__main__':
    params = {'dataType': '02', 'city': '3301', 'date': '201604', 'pageIndex': '1', 'orderType': '01', 'orderColumn': 'data_month', 'platform': '1', 'industry': 'EC0004'}
    p = 3300
    while True:
        p = p + 1
        params['city'] = str(p)
        params['date'] = '2016'
        total = getTotalPages()
        if total == 0:
            break
        sdir = Path('city_' + str(p))
        if not sdir.exists():
            sdir.mkdir()
        for i in range(1, 10):
            params['date'] = str(201600 + i)
            total = getTotalPages()
            sdir = Path('city_' + str(p)) / Path('date_' + params['date'])
            if not sdir.exists():
                sdir.mkdir()
            apart(sdir)
        


        
