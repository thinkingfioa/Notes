#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Point:
    def __init(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"  # 输出：Point 销毁


pt1 = Point()  # 解释：对象引用计数 + 1
pt2 = pt1  # 解释：对象引用计数 + 1
pt3 = pt1  # 解释：对象引用计数 + 1。该对象一共有3个引用
del pt1  # 解释：对象引用计数 - 1
del pt2  # 解释：对象引用计数 - 1
del pt3  # 解释：对象引用计数 - 1。对象引用为0，所以调用析构函数函数


class Employee:
    "所有员工的基类"
    empCount = 0  # 解释：是一个类变量，他的值在所有实例中共享

    def __init__(self, name, salary):  # 解释：构造函数
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary


emp1 = Employee("thinking", 19)
emp2 = Employee("ppp", 23)
emp1.displayEmployee()  # 输出：Name:  thinking , Salary:  19
emp2.displayEmployee()  # 输出：Name:  ppp , Salary:  23
emp1.displayCount()  # 输出：Total Employee 2

emp1.age = 7

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8)  # 添加属性 'age' 值为 8
setattr(emp1, 'salary', 15)
print emp1.age   # 输出: 8
emp1.displayEmployee()  # 输出：Name:  thinking , Salary:  15
