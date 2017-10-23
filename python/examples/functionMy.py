#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printmustargument(str):
    """必备参数"""
    print str
    return


str = "ppp"
printmustargument(str)  # 输出:ppp


def printkeywordargument(name, age):
    """关键字函数"""
    print "Name: ", name
    print "Age:", age


printkeywordargument(name="ppp", age=35)  # 输出: Name: ppp   Age: 35


def printdefaultargument(name, age=20):
    """缺省参数"""
    print "Name: ", name
    print "Age:", age


printdefaultargument(name="thinking_fioa")  # 输出: Name: thinking_fioa   Age: 20


def printmoreargument(arg1, *vartuple):
    """不定长参数"""
    print arg1
    for var in vartuple:
        print var
    return


printmoreargument(10)  # 输出：10
printmoreargument(10, 20, 30)  # 输出: (10, 20, 30)


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