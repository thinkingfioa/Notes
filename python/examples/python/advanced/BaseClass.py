#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector( %d, %d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print v1 + v2  # 输出: Vector( 4, 6)


class Parent:  # 定义父类方法
    parentAttr = 100

    def __init__(self):
        print "调用父类的构造函数"

    def parentMethond(self):
        print "调用父类的方法"

    def helloWorld(self):
        print "调用父类方法helloWorld"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性: ", Parent.parentAttr


class Child(Parent):  # 定义子类

    def __init__(self):
        print "调用子类构造函数方法"

    def childMethod(self):
        print "调用子类方法"

    def helloWorld(self):
        print "调用子类方法helloWorld"


c = Child()  # 输出: 调用子类构造函数方法
c.childMethod()  # 输出：调用子类方法
c.parentMethond()  # 输出：调用父类的方法
c.setAttr(200)
c.getAttr()  # 输出：父类属性: 200
c.helloWorld()  # 输出：调用子类方法helloWorld