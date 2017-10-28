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
    
    @staticmethod
    def displayClassEmpCount():
        print "类的属性: ", empCount
```
说明:

1. empCount变量是一个类变量，python类变量非常特殊，请参考下文：python类属性和实例属性
2. _\_init\_\_函数是构造函数
3. self代表类的实例，self在定义类的方法时必须有。调用时不必传入相应的参数
4. @staticmethod描述类的静态方法

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

##### Python对象销毁(垃圾回收)
1. python使用了引用计数来跟踪和回收垃圾
2. 当对象被创建时，就创建了一个引用计数，当这个对象的引用计数变为0时，它被垃圾回收
3. \_\_del\_\_在对象销毁的时候被调用，当对象不再被使用时也就是说该对象引用=0时，调用析构函数

##### 代码

```
a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
```

```
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
```

##### 类的继承
1. 类的继承语法: class 派生类名(基类名)
2. 继承基类的构造(\_\_init\_\_方法)不会被自动调用，需要在派生类的构造中亲自调用
3. 调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。
4. 如果调用类中普通函数，并不需要带上self参数
5. Python先在本类中查找调用的方法，找不到才去基类中找

##### 代码
```
class SubClassName (ParentClass1[, ParentClass2, ...]):
   '类的解释'
   class_suite
```
```
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
```

##### 方法重写
子类可以覆写父类中的方法
##### 代码
```
class Parent:  # 定义父类方法

    def __init__(self):
        print "调用父类的构造函数"

    def helloWorld(self):
        print "调用父类方法helloWorld"


class Child(Parent):  # 定义子类

    def __init__(self):
        print "调用子类构造函数方法"

    def helloWorld(self):
        print "调用子类方法helloWorld"


c.helloWorld()  # 输出：调用子类方法helloWorld
```

##### 基础重载方法
python提供一些通用的功能，可以在自己的类中重写：

|序号|方法描述|简单的调用|
|:---:|:---:|:---|
|1|\_\_init\_\_(self [,args...])|构造函数，调用方法: obj = className(args)|
|2|\_\_del\_\_(self)|析构方法，调用方法 : del obj|
|3|\_\_repr\_\_(self)|转化为供解释器读取的形式，调用方法:repr(obj)|
|4|\_\_str\_\_(self)|用于将值转化为适于人阅读的形式，调用方法: str(obj)|
|5|\_\_cmp\_\_(self, x)|对象比较 简单的调用方法:cmp(obj, x)|

##### 父子类判断和实例的类型判断(类似于java的instanceof关键字）
1. issubclass() - 布尔值判断一个类是另一个类的子类或子孙类。语法: issubclass(sub, sup)
2. isinstance(obj, class) - 布尔函数，如果obj是class类的实例对象或者是一个class子类的实例对象

##### 运算符重载
python支持运算符重载
##### 代码
```
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
```

##### 类属性与方法
##### 类的私有属性
\_\_privateAttrs: 两个下划线开头，声明该属性为私有，不能在类的外部被访问。
##### 类的方法
在类的内部，定义方法：需要用到关键字def，且方法第一个参数必须是self
##### 类的私有方法
\_\_privateMethod: 两个下划线开头，声明该方法是私有方法
##### 类的静态方法
@staticmethod来修饰，无需加参数self

##### 代码
```
class JustCounter:
    __secretCount = 0  # 对象私有变量

    def countObjectSecretCount(self):
        self.__secretCount += 1

    @staticmethod  # 类的静态方法
    def countClassSecretCount():
        JustCounter.__secretCount += 1

    def printObjectSecretCount(self):
        print "属性: ", self.__secretCount

    @staticmethod
    def printClassSecretCount():
        print "类的属性: ", JustCounter.__secretCount


counter1 = JustCounter()
counter2 = JustCounter()
counter1.countObjectSecretCount()
JustCounter.countClassSecretCount()
counter2.countObjectSecretCount()

print "对象1的", counter1.printObjectSecretCount()  # 输出: 对象1的属性:  1
print JustCounter.printClassSecretCount()  # 输出: 类的属性:  2
print "对象2的", counter2.printObjectSecretCount()  # 输出: 对象2的属性:  2
```

##### 单下划线、双下划线、头尾双下划线说明：
1. \_\_foo\_\_: 定义的是特列方法，类似 \_\_init\_\_() 之类的。
2. \_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
3. \_\_foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

##### 探讨Python的类属性和实例属性
##### 代码1
```
class AAA():  
    aaa = 10  
 
# 情形1   
obj1 = AAA()  
obj2 = AAA()   
print obj1.aaa, obj2.aaa, AAA.aaa   # 输出 10, 10, 10
 
# 情形2  
obj1.aaa += 2  
print obj1.aaa, obj2.aaa, AAA.aaa   # 输出 12, 10, 10
 
# 情形3  
AAA.aaa += 3  
print obj1.aaa, obj2.aaa, AAA.aaa  # 输出 12, 13, 13
```
问: 
因为aaa属性被称为类属性，既然是类属性，那么根据从C++/Java这种静态语言使用的经验来判断，类属性应该是为其实例所共享的。那么从类的层次改变aaa的值，自然其实例的aaa的值也应该变化？

##### 代码2
```
class JustCounter:
    __secretCount = 0

    def countObjectSecretCount(self):
        self.__secretCount += 1

    @staticmethod
    def countClassSecretCount():
        JustCounter.__secretCount += 1

    def printObjectSecretCount(self):
        print "属性: ", self.__secretCount

    @staticmethod
    def printClassSecretCount():
        print "类的属性: ", JustCounter.__secretCount


counter1 = JustCounter()
counter2 = JustCounter()
counter1.countObjectSecretCount()  # counter1.__secretCount = 1, JustCounter.__secretCount = 0, counter2没有属性: __secretCount
JustCounter.countClassSecretCount()   # counter1.__secretCount = 1, JustCounter.__secretCount = 1, counter2没有属性: __secretCount
counter2.countObjectSecretCount()  # counter1.__secretCount = 1, JustCounter.__secretCount = 1, counter2.__secretCount=2


print "对象1的", counter1.printObjectSecretCount()  # 输出: 对象1的属性:  1
print JustCounter.printClassSecretCount()  # 输出: 类的属性:  1
print "对象2的", counter2.printObjectSecretCount()  # 输出: 对象2的属性:  2

 # 动态的加属性
 counter1.name = "thinking_fioa"
 print counter1.name  # 输出: thinking_fioa
```

```
       JustCounter
            |
       -----------
      |           |  
  counter1     counter2

```
解释: 

1. 首先：self.__secretCount += 1，可以理解为三个步骤: 取值，加操作，赋值操作
2. counter1.countObjectSecretCount()代码中: counter1没有\_\_secretCount这个属性，所以它向上找到JustCounter类，成功找到，执行 +1，然后为对象counter1添加属性并赋值\_\_secretCount = 1。
3. JustCounter.countClassSecretCount()代码: 仅仅为JustCounter.\_\_secretCount = 1
4. counter2.countObjectSecretCount()代码中: counter2没有\_\_secretCount这个属性，所以它向上找到JustCounter类，成功找到，执行 +1，然后为对象counter2添加属性并赋值\_\_secretCount = 2。

##### 总结：
1. Python的类属性和实例属性与Java的完全不同。python是一个动态语言，我们不能用Java语言的类属性来理解Python的类属性。
2. 理解Python属性需要依赖查找树来理解。从下往上查找机制
3. Python是动态语言，可以动态添加和删除属性

___

### Python正则表达式


























