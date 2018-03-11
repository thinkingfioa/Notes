#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random;
import urllib2;
import time

from bs4 import BeautifulSoup
import re;

def getProxyIp():
    proxy=[]
    for i in range(1, 2, 1):#获取第一页100*(3-1)条内容
        url='http://www.xicidaili.com/nn/';
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Referer':'http://www.xicidaili.com/'
        }
        req=urllib2.Request(url, headers=headers)
        try:
            page=urllib2.urlopen(req).read().decode('utf-8')
            bs=BeautifulSoup(page, "html.parser")
            data=bs.find_all("td", limit=10000)
            ip_compile = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
            port_compile = re.compile(r'<td>(\d+)</td>')
            ip = re.findall(ip_compile, str(data))
            port = re.findall(port_compile, str(data))
            num =0
            for ip_one in ip:
                ip_port = ip_one+":"+port[num]
                print "IP-PORT:", ip_port
                proxy.append(ip_port)
                num = num+1
        except:
            continue
    print "ips count", len(proxy)
    return proxy


def getHtml(url, headers, proxies):
    random_userAgent= random.choice(headers)
    random_proxy = random.choice(proxies)
    # print "random_UserAgent", random_userAgent
    print "random_proxy", random_proxy
    print "url", url

    req = urllib2.Request(url)
    req.add_header('User-Agent', random_userAgent)
    req.add_header('GET', url)
    req.add_header('Host', 'www.baidu.com')
    req.add_header('referer', 'http://www.baidu.com/')

    proxy_support = urllib2.ProxyHandler({'http': random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

    html = urllib2.urlopen(url, timeout=10) # unit: s
    return html

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'
    ]

# proxy = getProxyIp()
proxy = ['101.132.121.157:9000', '113.200.88.237:61202', '120.78.78.141:8888', '116.19.96.131:9797', '218.20.54.114:9797', '122.114.31.177:808']
#urlList = ["http://blog.csdn.net/thinking_fioa/article/details/78265745", "http://blog.csdn.net/thinking_fioa/article/details/78270793", "http://blog.csdn.net/thinking_fioa/article/details/78306670"]
urlList = ["http://blog.csdn.net/thinking_fioa/article/details/79192474","http://blog.csdn.net/thinking_fioa/article/details/79110447"
           ,"http://blog.csdn.net/thinking_fioa/article/details/78972847","http://blog.csdn.net/thinking_fioa/article/details/79024261"
           ,"http://blog.csdn.net/thinking_fioa/article/details/78344645","http://blog.csdn.net/thinking_fioa/article/details/79087627"]
count = random.randint(1000, 2000)
print("共执行%d 次" % (count))
success_count = 0
for j in range(count):
    for tempUrl in urlList:
        try:
            html = getHtml(tempUrl, user_agents, proxy)
            print("%s ---- %d, [successCount]%d" % (tempUrl, j, success_count))
            success_count = success_count + 1
        except urllib2.HTTPError as e2:
            print 'urllib2.HTTPError'
            time.sleep(1)
        except urllib2.URLError as e1:
            print 'urllib2.URLError'
            if hasattr(e1, 'code'):
                print 'Error code:', e1.code
            elif hasattr(e1, 'reason'):
                print 'Reason:', e1.reason
            time.sleep(1)
        except Exception, e:
            print "happen Exception"
            print e
            time.sleep(1)
        time.sleep(0.2)
else:
    print("%s 共执行%d 次" % (tempUrl, count));
