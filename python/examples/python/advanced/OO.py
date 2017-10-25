#!/usr/bin/python
# -*- coding: UTF-8 -*-


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
