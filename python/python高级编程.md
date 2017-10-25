# Python高级编程
### 前言
```
@author 鲁伟林
Python高级编程，主要包括
学习网址：
gitHub地址：
```

---

### 面向对象

##### 创建类
1.  使用class语句来创建一个类
2.  基本语法

#####代码
```
class ClassName:
	"类的描述信息"
	class_suite
```

举例：
##### 代码
```
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
```
说明:

1. empCount变量是一个类变量，它的值在所有实例间共享
2. _\_init\_\_函数是构造函数
3. self代表类的实例，self在定义类的方法时必须有。调用时不必传入相应的参数

##### self代表类的实例，而非类

##### 创建实例代码
```
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
```

##### Python提供类似于java的反射
1. getattr(obj, name[, default]): 访问对象的属性
2. hasattr(obj, name): 检查是否存在一个属性
3. setattr(obj, name, value): 设置一个属性。如果属性不在，创建新的
4. delattr(obj, name): 删除属性

##### 代码
```
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
emp1.displayEmployee()  # 输出：Name:  thinking , Salary:  19
emp1.displayCount()  # 输出：Total Employee 1

emp1.age = 7

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8)  # 添加属性 'age' 值为 8
setattr(emp1, 'salary', 15)
print emp1.age   # 输出: 8
emp1.displayEmployee()  # 输出：Name:  thinking , Salary:  15
```
注:

```
python的面向对象关于对象的属性和java或C++不太一样。它的属性是依赖于对象实例，
如果是写在类里面的，如:empCount。是一个类变量，所有实例共享，和java语言中的static属性差不多
```

##### Python内置类属性
1. \_\_dict\_\_ : 类的属性（包含一个字典，由类的数据属性组成）
2. \_\_doc__ :类的文档字符串
3. \_\_name__: 类名
4. \_\_module__: 类定义所在的模块（类的全名是'\_\_main\_\_.className'，如果类位于一个导入模块mymod中，那么className.\_\_module\_\_ 等于 mymod）
5. \_\_bases\_\_ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）




















