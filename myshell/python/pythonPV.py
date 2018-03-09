#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;
import random;
import urllib2;

import urllib

from bs4 import BeautifulSoup
import re;

def getProxyIp():
    proxy=[]
    for i in range(1,3):#获取第一页100*(3-1)条内容
        url='http://www.xicidaili.com/nn/'+str(i);
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Referer':'http://www.xicidaili.com/'
        }
        req=urllib2.Request(url,headers=headers)
        try:
            page=urllib2.urlopen(req).read().decode('utf-8')
            bs=BeautifulSoup(page,"html.parser")
            data=bs.find_all("td", limit=40)
            ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
            port_compile = re.compile(r'<td>(\d+)</td>')
            ip = re.findall(ip_compile, str(data))
            port = re.findall(port_compile, str(data))
            num =0
            for ip_one in ip:
                ip_port = ip_one+":"+port[num]
                proxy.append(ip_port)
                num = num+1
        except:
            continue
    print "ips count", len(proxy)
    return proxy


proxy = getProxyIp()
#urlList = ["http://blog.csdn.net/thinking_fioa/article/details/78265745", "http://blog.csdn.net/thinking_fioa/article/details/78270793", "http://blog.csdn.net/thinking_fioa/article/details/78306670"]
urlList = ["http://blog.csdn.net/thinking_fioa/article/details/79192474"]
for tempUrl in urlList:
    count = random.randint(100, 300);
    print("%s 共执行%d 次" % (tempUrl, count));
    for j in range(count):
        try:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                'X-Forwarded-For': proxy[random.randint(0,len(proxy)-1)],
                'keep-alive': None}
            myrequest = urllib2.Request('http://blog.csdn.net/thinking_fioa/article/details/79192474', None, head)
            myresponse = urllib2.urlopen(myrequest)
            print("%s ---- %d" % (tempUrl, j))
        except Exception, e:
            print proxy
            print e
    else:
        print("%s 共执行%d 次" % (tempUrl, count));
