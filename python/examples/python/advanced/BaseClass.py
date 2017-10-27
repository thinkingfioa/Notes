#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Parent:  # 定义父类方法
    parentAttr = 100

    def __init__(self):
        print "调用父类的构造函数"

    def parentMethond(self):
        print "调用父类的方法"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性: ", Parent.parentAttr


class Child(Parent):  # 定义子类

    def __init__(self):
        print "调用子类构造函数方法"

    def childMethod(self):
        print "调用子类方法"


c = Child()  # 输出: 调用子类构造函数方法
c.childMethod()  # 输出：调用子类方法
c.parentMethond()  # 输出：调用父类的方法
c.setAttr(200)
c.getAttr()  # 输出：父类属性: 200