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

---

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

##### Python 列表
- 列表使用'[]'来标识
- List(列表)是Python中使用最频繁的数据类型。
- 列表的切割也可以用到变量 [头下标:尾下标]
- 加号(+)是字符串连接运算符，星号(*)是重复操作
- 列表允许更新，如 ：list[2] = 123;

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = [ "runoob", 786 , 2.23, "john", 70.2 ];
tinylist = [123, "john"];

print(list); #输出: ['runoob', 786, 2.23, 'john', 70.2]
print(list[0]); #输出: runoob
print(list[1:3]); #输出: [786, 2.23]
print(list[2:]); #输出: [2.23, 'john', 70.2]
print(tinylist *2 ); #输出: [123, 'john', 123, 'john']
print(list + tinylist); #输出: ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```

##### Python 元组
- 元组用'()'标识
- 元组是另一个数据类型，类似于List(列表)
- 元组不允许二次赋值，相当于只读列表。如：tuple[2] = 1000非法访问

```
tuply = ("runoob", 786 , 2.23, "john", 70.2 );
tinytuply = (123, "john");

print(tuply); #输出: ['runoob', 786, 2.23, 'john', 70.2]
print(tuply[0]); #输出: runoob
print(tuply[1:3]); #输出: [786, 2.23]
print(tuply[2:]); #输出: [2.23, 'john', 70.2]
print(tinytuply *2 ); #输出: [123, 'john', 123, 'john']
print(tuply + tinytuply); #输出: ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```

##### Python字典
- 字典用"{ }"标识。
- 类似于其他语言的：Map

```
dict = {};
dict["one"] = "This is one";
dict[2] = "This is two";

tinydict = {"name": "john", "code":6734, "dept":"sales"};

print(dict["one"]); # 输出: This is one
print(dict[2]); # 输出: This is two
print(tinydict); # 输出: {'dept': 'sales', 'code': 6734, 'name': 'john'}
print(tinydict.keys()); # 输出: ['dept', 'code', 'name']
print(tinydict.values()); # 输出: ['sales', 6734, 'john']
```

##### Python数据类型转换
- int('12', 16),就是说：12是一个16进制的。输出为: 18.

|函数|描述|
|:---:|:---:|
|int(x [,base])|将x转换为一个整数|
|long(x [,base] )|将x转换为一个长整数|
|float(x)|将x转换到一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象 x 转换为字符串|
|repr(x)|将对象 x 转换为表达式字符串|
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象|
|tuple(s)|将序列 s 转换为一个元组|
|list(s)|将序列 s 转换为一个列表|
|set(s)|转换为可变集合|
|dict(d)|创建一个字典。d 必须是一个序列 (key,value)元组|
|frozenset(s)|转换为不可变集合|
|chr(x)|将一个整数转换为一个字符|
|unichr(x)|将一个整数转换为Unicode字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

---

### Python 运算符

##### Python算术运算符
|运算符|描述|举例|
|:---:|:---:|:---:|
|**	|幂|a**b 为10的20次方， 输出结果 100000000000000000000|
|//|取整除|9//2 输出结果 4 , 9.0//2.0 输出结果 4.0|

##### Python逻辑运算符
|运算符|描述|举例|
|:---:|:---:|:---:|
|and|x and y|布尔"与", 类似于: &&|
|or|x or y|布尔"或", 类似于:或|
|not|not x|布尔"非", 类似于: !|

##### Python 成员运算符
|运算符|描述|
|:---:|:---:|
|in|如果在指定的序列中找到值返回 True，否则返回 False|
|not in|如果在指定的序列中没有找到值返回 True，否则返回 False|

```
a = 7;
b = 2;
list = [1,2,3,4,5];

if(a in list):
	print("a is in list");
else:
	print(" a is not list"); # 输出

if(b in list):
	print("b is in list"); # 输出
else:
	print("b is not list");
```

##### Python 身份运算符
- is是传递地址
- == 是比较值。

|运算符|描述|
|:---:|:---:|
|is|is 是判断两个标识符是不是引用自一个对象|
|is not|is not 是判断两个标识符是不是引用自不同对象|

```
//运用脚本运行，是同一个对象。
a = 7;
b = 7;

if(a is b):
	print("a is b"); # 输出
else:
	print(" a is not list"); 

b = 10;
if(a is b):
	print("a is b"); 
else:
	print("a is not b"); # 输出
```

---

### Python条件语句
```
if 判断语句1:
    执行语句....;
elif 判断语句2:
    执行语句....;
else:
    执行语句3;
```

```
num = 9
if(num >= 0 and num <= 10):    # 判断值是否在0~10之间
    print 'hello'; # 输出结果: hello
```

---

### Python 循环语句

##### Python的While语句

```
numbers = [12, 37, 5, 42, 8, 3];
even = [];
odd = [];
while(len(numbers) > 0):
    number = numbers.pop();
    if(number%2==0):
        even.append(number);
    else:
        odd.append(number);
```

##### Python的While-else语句 
- 当while后的条件不满足时，执行:else语句

```
count = 0
while(count < 5):
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
```

##### Python的for循环语句
```
for(letter in 'Python'):     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for(fruit in fruits):        # 第二个实例
   print '当前水果 :', fruit
 
print "Good bye!"
```

##### Python的for-else语句 
- 当for后的条件不满足时，执行:else语句

---

### Python的pass语句
- pass是空语句，为了保证程序结构的完整性。
- pass不做任何事，一般用作占位符

---

### Python Number(数字)
- Python支持: int(有符号整型), long(长整型: 3291930L), float(浮点型), complex(复数: a+bj 或者 complex(a,b).
- 可以使用del语句删除对象的引用. 如: del var1, var2;

##### Python数据类型转换
- int('12', 16),就是说：12是一个16进制的。输出为: 18.

|函数|描述|
|:---:|:---:|
|int(x [,base])|将x转换为一个整数|
|long(x [,base] )|将x转换为一个长整数|
|float(x)|将x转换到一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象 x 转换为字符串|
|repr(x)|将对象 x 转换为表达式字符串|
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象|
|tuple(s)|将序列 s 转换为一个元组|
|list(s)|将序列 s 转换为一个列表|
|set(s)|转换为可变集合|
|dict(d)|创建一个字典。d 必须是一个序列 (key,value)元组|
|frozenset(s)|转换为不可变集合|
|chr(x)|将一个整数转换为一个字符|
|unichr(x)|将一个整数转换为Unicode字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

##### Python数学函数
|函数|描述|
|:---:|:---:|
|abs(x)|返回数字的绝对值，如abs(-10) 返回 10|
|cmp(x, y)|如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1|
|exp(x)|返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045|
|fabs(x)|返回数字的绝对值，如math.fabs(-10) 返回10.0|
|ceil(x)|返回数字的上入整数，如math.ceil(4.1) 返回 5|
|floor(x)|返回数字的下舍整数，如math.floor(4.9)返回 4|
|log(x)|如math.log(math.e)返回1.0,math.log(100,10)返回2.0|
|log10(x)|返回以10为基数的x的对数，如math.log10(100)返回 2.0|
|max(x1, x2,...)|返回给定参数的最大值，参数可以为序列。|
|min(x1, x2,...)|返回给定参数的最小值，参数可以为序列。|
|modf(x)|返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。|
|pow(x, y)|x**y 运算后的值。|
|round(x [,n])|返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。|
|sqrt(x)|返回数字x的平方根|

##### Python随机数函数
|函数|描述|
|:---:|:---:|
|choice(seq)|从序列的元素中随机挑选一个元素，如random.choice(range(10))，从0到9中随机挑选一个整数|
|randrange|([start,] stop [,step])从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1|
|random()|随机生成下一个实数，它在[0,1)范围内|
|seed([x])|改变随机数生成器的种子seed|
|shuffle(list)|将序列的所有元素随机排序|
|uniform(x, y)|随机生成下一个实数，它在[x,y]范围内|

##### Python数学常量
|常量|描述|
|:---:|:---:|
|pi|数学常量pi(圆周率)|
|e|数学常量e，e是自然数|

---

### Python字符串
##### Python字符串格式化
|符号|描述|
|:---:|:---:|
|%c|格式化字符及其ASCII码|
|%s|格式化字符串|
|%d|格式化整数|
|%u|格式化无符号整型|
|%o|格式化无符号八进制数|
|%x|格式化无符号十六进制数|
|%X|格式化无符号十六进制数（大写）|
|%f|格式化浮点数字，可指定小数点后的精度|
|%e|用科学计数法格式化浮点数|
|%E|作用同%e，用科学计数法格式化浮点数|
|%g|%f和%e的简写|
|%G|%f 和 %E 的简写|
|%p|用十六进制数格式化变量的地址|

##### Python三引号
- 三引号(""")可以将字符串变成多行，且字符串中可以包括一些特殊字符

##### Python的字符串内建函数

|方法|描述|
|:---:|:--:|
|string.capitalize()|把字符串的第一个字符大写|
|string.center(width)|返回一个原字符串居中,并使用空格填充至长度width的新字符串|
|string.count(str, beg=0, end=len(string))|返回str在string 里面出现的次数|
|string.decode(encoding='UTF-8',errors='strict')|以encoding 指定的编码格式解码 string|
|string.encode(encoding='UTF-8', errors='strict')|以encoding指定的编码格式编码string|
|string.endswith(obj, beg=0, end=len(string))|检查字符串是否以obj结束,如果在指定的范围内以obj结束，返回 True|
|string.expandtabs(tabsize=8)|把字符串string中的tab符号转为空格，tab符号默认的空格数是8|
|string.find(str, beg=0, end=len(string))|检测str是否包含在string中，如果是返回开始的索引值，否则返回-1|
|string.format()|格式化字符串|
|string.index(str, beg=0, end=len(string))|跟find()方法一样，只不过如果str不在 string中会报一个异常.|
|string.isalnum()|如果string 至少有一个字符并且所有字符都是字母或数字则返回 True|
|string.isalpha()|如果 string 至少有一个字符并且所有字符都是字母则返回 True|
|string.isdigit()|如果 string 只包含数字则返回 True|
|string.isnumeric()|如果 string 中只包含数字字符，则返回 True|
|string.isspace()|如果 string 中只包含空格，则返回 True|
|string.isupper()|如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True|
|string.join(seq)|以 string 作为分隔符，将 seq 中所有的元素合并为一个新的字符串|
|string.ljust(width)|返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串|
|string.lower()|转换 string 中所有大写字符为小写.|
|string.lstrip()|截掉 string 左边的空格|
|string.rstrip()|删除 string 字符串末尾的空格.|
|string.strip([obj])|在 string 上执行 lstrip()和 rstrip()|
|max(str)|返回字符串 str 中最大的字母。|
|min(str)|返回字符串 str 中最小的字母。|
|string.partition(str)|有点像 find()和 split()的结合体,从str出现的第一个位置起,把字符 串string分成一个3元素的元组(string_pre_str,str,string_post_str),如果string中不包含str 则 string_pre_str == string.|
|string.replace(str1, str2,  num=string.count(str1))|把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.|
|string.rfind(str, beg=0,end=len(string) )|类似于 find()函数，不过是从右边开始查找.|
|string.rjust(width)|返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串|
|string.rpartition(str)|类似于 partition()函数,不过是从右边开始查找.|
|string.split(str="", num=string.count(str))|以str为分隔符切片string，如果num有指定值，则仅分隔num个子字符串|
|string.splitlines([keepends])|按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。|
|string.startswith(obj, beg=0,end=len(string))|检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
|string.swapcase()|翻转 string 中的大小写|
|string.upper()|转换 string 中的小写字母为大写|
|string.zfill(width)|返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0|

---

### Python列表
- 列表的数据项不需要具有相同的类型

##### 删除列表元素

```
list = ["thinking", "fioa", 123, 456];
print list # 输出: ['thinking', 'fioa', 123, 456]
del list[2]
print list # 输出: ['thinking', 'fioa', 456]
```

##### Python列表截取
|表达式|结果|描述|
|:---:|:---:|:---:|
|L[2]|'fioa'|读取列表中第三个元素|
|L[-2]|123|读取列表中倒数第二个元素|
|L[1:]|['fioa', 123, 456]|从第二个元素开始截取列表|

```
list2 = ["thinking", "fioa", 123, 456]
print list2[2]  # 输出 123
print list2[-3]  # 输出 fioa
print list2[1:]  # 输出 ['fioa', 123, 456]
```

---

### Python元组
- 元组只有一个元素，需要在元素后面添加逗号。如：tup1 = (50,);
- 元组不能修改，意味着元组不能删除，更新等更改型操作。

---

### Python字典

##### 删除字典元素
- 能删除单一的元素，也能删除整个字典。还可以清空整个字典。
- 键必须不可变，所以可以用数字，字符串或元组充当。但是列表不能作为key。

```
dict = {"Name": "thinking", "age":18, "lover":"ppp"}
print dict  #输出 {'age': 18, 'Name': 'thinking', 'lover': 'ppp'}
del dict["lover"]
print dict  #输出 {'age': 18, 'Name': 'thinking'}
dict.clear()
del dict
```

---

### Python日期和时间
- Python提供了time和calendar模块用于格式化时间和日期。
- 时间间隔是以秒为单位的浮点数。

```
ticks = time.time()
print ticks  # 输出：1508668369.94
```

##### 格式化日期
- 使用time模块的strftime方法来格式化日期

```
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 输出: 2017-10-22 18:36:56
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  # 输出: Sun Oct 22 18:36:56

# 将格式化转换成时间戳
a = "Sun Oct 22 18:36:56 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))  # 输出: 1508668616.0
```

##### 获取某月日历

```
cal = calendar.month(2017, 2)
'''输出：
   February 2017
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28
'''
print cal
```

---

### Python函数

##### 定义一个函数
- 函数代码块以def关键字开头，后接函数标识符号名称和圆括号()
- 任何**传入参数和自变量**必须放在圆括号中间。圆括号之间可以用于定义参数
- 函数的第一行语句可以选择性地使用文档字符串(用于存放函数说明)
- 函数内容以冒号起始，并且缩进
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None

```
def functionname(parameters):
    """函数说明"""
    function_suite
    return [expression]
    
```

##### 函数调用
```
def printme(str):
    """打印任何传入的字符串"""
    print str
    return


printme("thinking")  # 输出：thinking
printme("fioa")  # 输出：fioa
```

##### 参数传递
在Python中，string，tuples和numbers是不可更改的对象，而list, dict等则是可修改的对象.

- 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个int值的对象10，再让a指向它，5就被丢弃。
- 可变类型：变量赋值 la=[1,2,3,4]后再赋值la[2]=5则是将list la的第三个元素更改了。

python函数的参数传递:

- 不可变类型：类似于c++的值传递，如整数，字符串，元组。如fun(a)，传递的只是a的值。如果在函数内部修改了a的值，对传入的值没有任何影响.
- 可变类型：类似C++的引用传递，如列表。如fun(la)传入，函数内部修改了la，对传入的值有影响。

##### python传不可变对象实例
```
def changeint(a):
    a = 10


b = 2
changeint(b)
print b  # 结果: 2
```

##### python传可变对象实例
```
def changelist(mylist):
    mylist.append("thinking")
    return
    

mylist = [1, 2, 3]
print mylist  # 输出：[1, 2, 3]
changelist(mylist)
print mylist  # 输出：[1, 2, 3, 'thinking']
```

**总结:**

- 不可变类型(string, number, tuples)作为参数传值到函数中，如果在函数中修改，**无效**。
- 可变类型(list, dict)作为参数传值到函数中，如果在函数中修改，**有效**。

##### 函数参数
调用函数时可使用的参数类型

- 必备参数
- 关键字参数
- 缺省参数
- 不定长参数

##### 必备参数
想调用函数，必须传入对应的参数

```
def printmustargument(str):
    """必备参数"""
    print str
    return


str = "ppp"
printmustargument(str)  # 输出:ppp
```

##### 关键字参数
使用关键字参数，允许调用函数时参数的顺序可以不一致。

```
def printkeywordargument(name, age):
    """关键字函数"""
    print "Name: ", name
    print "Age:", age


printkeywordargument(name="ppp", age=35)  # 输出: Name: ppp   Age: 35
```

##### 缺省参数
调用函数时，缺省参数没有传入，使用默认值

```
def printdefaultargument(name, age=20):
    """缺省参数"""
    print "Name: ", name
    print "Age:", age


printdefaultargument(name="thinking_fioa")  # 输出: Name: thinking_fioa   Age: 20
```

##### 不定长参数
函数接受任意长度的参数

```
def printmoreargument(arg1, *vartuple):
    """不定长参数"""
    print arg1
    for var in vartuple:
        print var
    return


printmoreargument(10)  # 输出：10
printmoreargument(10, 20, 30)  # 输出: (10, 20, 30)
```

---

### 匿名函数
python使用lambda来创建匿名函数

- lambda只是一个表达式，函数体比def简单很多
- lambda函数拥有自己的命名空间，除了自有参数列表和全局命名空间里的参数外，其他都不能访问

##### 语法

- lambda [arg1 [, arg2,... argn]]: expression

```
sum = lambda arg1, arg2: arg1 + arg2

print "sum is: ", sum(10, 20)  # 输出： 30
```

---

### return语句
- return语句[表达式]，将计算结果返回

```
def sumtwonumber(arg1, arg2):
    return arg1+arg2


print sumtwonumber(100, 200)  # 输出: 300
```

---

### 变量作用域
- 全局变量：定义在函数外的变量
- 局部变量：定义在函数内的变量，只能在函数内部访问。
- 全局变量想作用与函数内，需要加一个global

```
total = 1


def sumtwonumber(arg1, arg2):
    total = arg1 + arg2
    print "函数内total: ", total  # 输出: 函数内total: 300
    return total


sumtwonumber(100, 200)  # 输出: 300
print "全局变量: ", total  # 输出: 全局变量: 1
```


















