#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num  # 输出：电话号码是:  2004-959-559
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是: ", num  # 输出： 电话号码是:  2004959559


line2 = "Cats are smarter than dogs"
matchObj = re.match('dogs', line2, re.M | re.I)

if matchObj:
    print "match --> matchObj.group(): ", matchObj.group()
else:
    print "No match!"  # 输出: No match!

searchObj = re.search('dogs', line2, re.M | re.I)

if searchObj:
    print "match --> matchObj.group(): ", searchObj.group()  # 输出：match --> matchObj.group():  dogs
else:
    print "search --> searchObj.group(): ", searchObj.group()


print re.match('www', "www.baidu.com").span()  # 输出: (0, 3)

line = "Cats are smarter than dogs"

matchObj = re.search('(.*) are (.*?) (.*)', line, re.I)  # 解释: ? 有非贪婪意思

if matchObj:
    print "matchObj.group() : ", matchObj.group()  # 输出: Cats are smarter than dogs
    print "matchObj.group(1) : ", matchObj.group(1)  # 输出: Cats
    print "matchObj.group(2) : ", matchObj.group(2)  # 输出: smarter
    print "matchObj.group(3) : ", matchObj.group(3)  # 输出: than dogs
else:
    print "No match!!"
