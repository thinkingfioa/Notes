# Python基本语法
 Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。
 
 ---
 
    Python语法的后缀名是以.py结尾，文件开头是:
    #!/usr/bin/python 或 #!/usr/bin/env python
    如果支持中文，请改成:
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-

 ---

### Python 基础语法

##### Python如何执行
- 使用交互是界面执行。
- 使用python test.py命令执行
- 利用./test.py执行

##### Python 标识符
- 以单下划线开头的属性，表示是类的私有属性(包括方法，变量)。如:_foo表示不能直接访问的类属性。
- 以双下划线开头的 __foo 代表类的私有成员；
- 以双下划线开头和结尾的 _ _ foo _ _ 代表Python 里特殊方法专用的标识，如 _ _ init _ _() 代表类的构造函数。

##### 行和缩进
- 学习Python与其他语言最大的区别：Python不使用{}来控制，而使用缩进来使用模块。
- 要注意区别4个空格和Tab键。很容易导致执行出错。

```Python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "hello world";

if True:
    print("Answer:");
    print("true");
else:
    print("Answer:");
    # 没有严格缩进，在执行时会报错
  print("false");
```

##### Python引号
- Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串。
- 三引号(""")可以由多行组成，是编写多行文本的快捷语法，常用于文档字符串。

##### Python注释
- python中单行注释采用 # 开头
- python 中多行注释使用三个单引号(''')或三个双引号(""")

##### Python空行
- 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

##### Print输出
- print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号。

```
//换行
print("hello");
//不换行
print("hello"),
print("world");
```

##### 多个语句组成的代码组
- 缩进相同的一组语句构成一个代码块，我们称之代码组。
- 子句: 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。

```
if expression: 
   suite 
elif expression:
   suite  
else:
   suite 
```

### Python变量类型
变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。

##### Python变量赋值
- 变量赋值不需要类型声明
- 每个变量在使用前必须赋值，变量赋值以后该变量才会被创建

```
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
print(count),
print(miles),
print(name);
```

##### 多个变量赋值

```
a = b = c = 1;
a, b, c = 1,2, "thinking";
```

##### 标准数据类型
- Numbers(数字)
- String(字符串)
- List(列表)
- Tuple(元组)
- Dictionary(字典)

##### Python数字(Numbers)
- Python支持: int(有符号整型), long(长整型: 3291930L), float(浮点型), complex(复数: a+bj 或者 complex(a,b).
- 可以使用del语句删除对象的引用. 如: del var1, var2;

##### Python字符串(String)
- 如果想实现字符串截取，可以使用变量 [头下标:尾下标]。
- 加号(+)是字符串连接运算符，星号(*)是重复操作

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

str = "Hello World!";

print(str); #输出: Hello World!
print(str[0]); # 输出: H
print(str[2:5]); # 输出: llo
print(str[2:]); # 输出: llo World!
print(str * 2); # 输出2遍: Hello World!Hello World!
print(str + " TEST"); # 输出: Hello World! TEST
```

























