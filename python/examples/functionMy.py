#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printme(str):
    """打印任何传入的字符串"""
    print str
    return


printme("thinking")  # 输出：thinking
printme("fioa")  # 输出：fioa


def changeint(a):
    a = 10


b = 2
changeint(b)
print b  # 结果: 2


def changelist(mylist):
    mylist.append("thinking")
    return


mylist = [1, 2, 3]
print mylist  # 输出：[1, 2, 3]
changelist(mylist)
print mylist  # 输出：[1, 2, 3, 'thinking']