#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

ticks = time.time()
print ticks  # 输出：1508668369.94

print "--------------------------------------"

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 输出: 2017-10-22 18:36:56
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  # 输出: Sun Oct 22 18:36:56

# 将格式化转换成时间戳
a = "Sun Oct 22 18:36:56 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))  # 输出: 1508668616.0

cal = calendar.month(2017, 2)
'''输出：
   February 2017
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28
'''
print cal