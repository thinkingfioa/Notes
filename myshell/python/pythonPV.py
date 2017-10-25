#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;
import random;
import urllib2;

#使用build_opener()是为了让python程序模仿浏览器进行访问  
opener = urllib2.build_opener()  
opener.addheaders = [('User-agent', 'Mozilla/5.0')]  

#urlList = ["http://blog.csdn.net/thinking_fioa/article/details/78265745", "http://blog.csdn.net/thinking_fioa/article/details/78270793", "http://blog.csdn.net/thinking_fioa/article/details/78306670"]
urlList = ["http://blog.csdn.net/thinking_fioa/article/details/78344645"]
#tempUrl = raw_input("请输入网址:");
for tempUrl in urlList:
    count = random.randint(300, 400);
    print("%s 共执行%d 次" % (tempUrl, count));
    for j in range(count):  
	    try :  
	        opener.open(tempUrl)
	        print("%s ---- %d" % (tempUrl, j))
	    except urllib2.error.HTTPError:  
	    	print('urllib2.error.HTTPError')
	    	time.sleep(1)  
	    except urllib2.error.URLError:
			print('urllib2.error.URLError')
			time.sleep(1)
	    time.sleep(0.2)
    else:
    	print("%s 共执行%d 次" % (tempUrl, count));
