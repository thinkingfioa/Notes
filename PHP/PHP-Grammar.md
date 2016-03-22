#PHP-Grammar Study
```
<?php
    //此处是php代码
?>
```
###PHP注释
- 注释与java差不多，但增加一个单行注释: #。

###PHP变量（大小写敏感）
- PHP是一门类型松散的语言，不必告知变量的数据类型。
- 变量以$符号开头，其后加变量名称
- 变量名称以字母或下划线开头
- 变量名称不能以数字开头
- 变量名称只能包含字母数字字符和下划线(A-z、0-9 以及_)
- 所有用户定义的**函数，类和关键字**(eg:if else,echo, so on) 都对大小写不敏感,**变量对大小写敏感**。

- 变量作用域: local，global，static
	- global:关键字用于访问函数外的全局变量。**函数内部要使用全局变量，必须在变量前加global。**
```php
<?php
	$x=thinking;
	$y=fioa;
	function Test(){}
		global $x,$y;
 		$y=$x+$y;
		Or
		$GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y']; //$GLOBALS[index]保存了所有了全局变量（超全局变量）
	}
?>
```
	- PHP  关键字: **static **,在使用修饰符static修饰的局部变量后，变量仍然是局部变量，但是会保存起来，下次可以直接使用，值还是最后一次使用的值。
	
###PHP的输出
- print:Print只能接收一个参数
- echo：可以多参数
- PHP语言中使用**var_dump($cars)**来输出变量的具体。

#PHP字符串函数
- strlen() 返回字符串长度
- strpos("hello world","world") 返回world在helloworld的首个匹配字符串的位置

### PHP常量
- 定义方式：define()函数，有三个参数：
	1.首个参数定义常量的名称；
	2.第二个参数定义常量的值；
	3.定义常量名是否对大小写不敏感，true为不敏感，false为敏感（默认）。
- 常量使用时名称前没有$符号。
- 与变量不同，常量贯穿整个脚本是自动全局的。

###PHP比较运算符：其它与Java一样，特意留意下面两种

	===  全等（完全相同），即值相同和类型相同
	!== 不全等（不完全相同）

###PHP数组运算符
- 说明：PHP中，数组其实就是一个key-value对
- **+** 将两个数组联合，但不覆盖重复的键，以前面的数组为准。
- **==** 相等拥有相同的键值对
- **!=** 不相等
- **===** 全等 拥有相同的键值对，且键值对的顺序也相同，则返回true
- **!==** 不全等

###数组（索引数组，关联数组，多维数组）
- count() 获取数组的长度
- sort() - 以升序对数组排序（不要对关联数组使用，否则会抹去Key）
- rsort() - 以降序对数组排序（不要对关联数组使用，否则会抹去Key）
- sort()和rsort()用于索引数组的排序
- asort() - 根据值，以升序对关联数组进行排序
- ksort() - 根据键，以升序对关联数组进行排序
- arsort() - 根据值，以降序对关联数组进行排序
- krsort() - 根据键，以降序对关联数组进行排序

```PHP
<?php
$age=array("Bill"=>"35","Steve"=>"37","Peter"=>"43");//关联数组

foreach($age as $x=>$x_value) {
  echo "Key=" . $x . ", Value=" . $x_value;
  echo "<br>";
}
?>
```

#超全局变量

**$GLOBALS** 引用全局作用域中可用的全部变量
**$_SERVER** 保存关于报头、路径和脚本位置的信息
**$_REQUEST** 用于收集 HTML 表单提交的数据
**$_POST** 广泛用于收集提交 method="post" 的 HTML 表单后的表单数据。$_POST 也常用于传递变量。
**$_GET** 用于收集提交 HTML 表单 (method="get") 之后的表单数据。
**$_COOKIE**
**$_SESSION**

**$_SERVER["PHP_SELF"]** 返回当前执行脚本的文件名
使用**$_SERVER["PHP_SELF"]**可以将表单提交到页面本身


判断页面是否已经提交过
	$_SERVER["REQUEST_METHOD"] == "POST"
表单：
PHP $_REQUEST 用于收集 HTML 表单提交的数据。
PHP $_POST 广泛用于收集提交 method="post" 的 HTML 表单后的表单数据。$_POST 也常用于传递变量。
PHP $_GET 也可用于收集提交 HTML 表单 (method="get") 之后的表单数据。
$_GET 也可以收集 URL 中的发送的数据。如<a href="test_get.php?subject=PHP&web=W3school.com.cn">测试 $GET</a>问号后面的数据

表单验证：
对于php中的表单，一般需要做几个验证：
通过 PHP trim($data) 函数去除用户输入数据中不必要的字符（多余的空格、制表符、换行）
通过 PHP stripslashes($data) 函数删除用户输入数据中的反斜杠（\）
通过htmlspecialchars($data)函数把特殊字符转换为 HTML 实体
```
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
```
通过empty($data)函数判断数据是否为空
通过preg_match(reg,$data)判断数据与正则表达式是否匹配

#PHP cookies

###创建cookies
setcookies()函数用于设置cookies，必须位于`<html>`标签之前。
setcookies(name,value,expire,path,domain);
要删除cookies，使expire重新设置成过期的时间即可。

###取回cookies
$_COOKIE["name"];


#PHP Sessions

###启动会话

session_start() 函数必须位于	`<html>`标签之前
设值：$_SESSION[name] = ?;

###终结Session

session_destory();
删除某个session数据：
unset($_SESSION[name]);


#PHP函数
###Debug可能用到的函数:
```
var_dump($a); //显示变量a的类型以及值
```
###字符串处理
```
**trim()** 去除用户输入数据中不必要的字符（多余的空格、制表符、换行）

**stripslashes()** 删除用户输入中的反斜杠

**preg_match(pattern,string)** 检索字符串的模式是否匹配
```
###日期
```
**date(format,timestamp)** 把时间戳格式转化为更易读的日期和时间，timestamp可选，默认为当前时间

**date_default_timezone_set()** 设置时区

**mktime(hour,minute,second,month,day,year)** 创建时间

**strtotime(time,now)** 用字符串来创建日期  
```



#PHP的文件可以引入，类似与java中 import功能
服务器端包含（SSI） 用于创建可在多个页面重复使用的函数、页眉、页脚或元素
###include & require

在PHP文件中插入（相当于**复制**）另一个PHP文件（在服务器执行它之前）

语法：
 include 'filename';
 require 'filename';

两者的不同在于错误处理方面：
 - require 会生成致命错误并停止运行脚本
 - include只会生成警告，并且脚本会继续

#类

## 类的定义
```php
class classname [ extends baseclass ] [ implements interfacename,[interfacename,...] ]
{
	[ use traitname, [ traitname, ... ]; ]
	[ visibility $property [ = value ]; ... ]
	[ function functionname (args) {
		// code
		}
		...
	]
}
```
和Java一样，能够继承类和实现接口
类名是大小写不敏感的。

###访问属性和方法
```php
$object->propertyname
$object->methodname(arg0,...);
```

###定义方法
```php
class Person
{
	public $name = '';
	function getName()
	{
		return $this->name;
	}
	function setName($newName)
	{
		$this->name = $newName;
	}
}
```

静态方法的调用（使用static修饰词）
```php
ClassName::staticMothodName(...);
```
如果一个函数用final关键字修饰，那么子类不能覆写该方法。

修饰符：
**public**:默认，可以在任何地方被访问；
**private**:只能被其定义所在的类访问；
**protected**:可以被其自身以及其子类访问。

###定义属性
可以为属性设置默认值，但是默认值必须是简单的常量。属性也可以使用上述的三个修饰词进行访问控制。
```php
public $name = "J Doe";// works
public $age = 0;// works
public $day = 60 * 60 * 24; // doesn't work
```

静态变量的访问：（使用static修饰词）
在类外访问：
```php
	ClassName::$propertyName
```
在类内访问：
```php
	self::$propertyName
```

###定义常量
在类外使用**ClassName::ConstantName**;
在类的方法里面可以使用**self**关键字，**self::ConstantName**。
类常量通常大写。
```php
class PaymentMethod
{
	const TYPE_CREDITCARD = 0;
	const TYPE_CASH = 1;
}
echo PaymentMethod::TYPE_CREDITCARD;
0
```
###对象创建
```
$object = new Class;
```
也可以：
```
$class = "Class";
$object = new $class;
```
在调用函数的时候也可以：
```
$class = new Class;
$object = "Class";
${$object}->init(50000,1.10);//相当于$class->init
```

###对象的赋值

对象传递的是引用：
```
$f = new Person("Fred", 35);
$b = $f; // $b and $f point at same object
$b->setName("Barney");
printf("%s and %s are best friends.\n", $b->getName(), $f->getName());
Barney and Barney are best friends.
```

如果要实现复制：
```
$f = new Person("Fred", 35);
$b = clone $f; // make a copy
$b->setName("Barney");// change the copy
printf("%s and %s are best friends.\n", $b->getName(), $f->getName());
Fred and Barney are best friends.
```

##继承

使用**extend**关键字

当需要访问一个对象的父类的被覆写的方法，使用**parent::methodName()**,不能使用**ParentClassName::methodName()**。如果使用子类自己的方法，使用**self::methodName()**;

同样可以使用**instanceof**关键字


##接口

和Java语法一样

##Traits（特性？）

```php
trait traitname [ extends baseclass ]
{
[ use traitname, [ traitname, ... ]; ]
[ visibility $property [ = value ]; ... ]
}
[ function functionname (args) {
// code
}
...
]
```

Traits提供在类外面的代码重用机制，Traits能够允许在不同类之间共享一些方法，这些类不需要有公共的父类。（相当于在Java类中要引用另一个Java类的对象）
```php
trait Logger
{
	public log($logString)
	{
		$className = __CLASS__;
		echo date("Y-m-d h:i:s", time()) . ": [{$className}] {$logString}";
	}
}

class User
{
	use Logger;
	public $name;
	function __construct($name = '')
	{
		$this->name = $name;
		$this->log("Created user '{$this->name}'");
	}
	
	function __toString()
	{
		return $this->name;
	}
}

class UserGroup
{
	use Logger;
	public $users = array();
}

public addUser(User $user)
{
	if (!$this->includesUser($user)) {
		$this->users[] = $user;
		$this->log("Added user '{$user}' to group");
	}
}

$group = new UserGroup;
$group->addUser(new User("Franklin"));
2012-03-09 07:12:58: [User] Created user 'Franklin'
2012-03-09 07:12:58: [UserGroup] Added user 'Franklin' to group
```

```php
trait First
{
	public doFirst()
	{
		echo "first\n";
	}
}
trait Second
{
	public doSecond()
	{
		echo "second\n";
	}
}
trait Third
{
	use First, Second;
	public doAll()
	{
	$this->doFirst();
	$this->doSecond();
	}
}
class Combined
{
	use Third;
}
$object = new Combined;
$object->doAll();
first
second
```
Traits也可以使用use来包含其他的Traits，但如果使用的Traits中的方法由重名，那么需要指定到底使用那个方法，使用**insteadof**关键字。同时，我们还可以给方法名取一个别名，使用**as**关键字。

```php
trait Command
{
	function run()
	{
		echo "Executing a command\n";
	}
}
trait Marathon
{
	function run()
	{
		echo "Running a marathon\n";
	}
}
class Person
{
	use Command, Marathon {
		Command::run as runCommand;
		Marathon::run insteadof Command;
	}
}

$person = new Person;
$person->run();
$person->runCommand();
Running a marathon
Executing a command
```

##抽象函数
不能提供默认的实现；
Traits也可以定义抽象函数，包含了Trait的类也必须实现Trait中的抽象函数。

##构造函数
```php
class Person
{
	function __construct($name, $age)
	{
		$this->name = $name;
		$this->age = $age;
	}
}

class Employee extends Person
{
	public $position, $salary;
	function __construct($name, $age, $position, $salary)
	{
		parent::__construct($name, $age);//不要使用父类的类名，使用parent关键字
		$this->position = $position;
		$this->salary = $salary;
	}
}

```
##析构函数
```php
class Building
{
	function __destruct()
	{
		echo "A Building is being destroyed!";
	}
}
```
##类检查

###类是否存在

**class_exists(classname)**判断类是否存在，返回Boolean值。
**get_clared_classes()**返回一个已经定义的类数组，使用**in_array()**来判断类是否数组中
```php
$doesClassExist = class_exists(classname);
$classes = get_declared_classes();
$doesClassExist = in_array(classname, $classes);
```

###得到类中的方法和属性
包括了从父类中继承的方法和属性，参数可以是一个字符串，也可以是直接是类名（不加引号）。
```php
//返回方法名组成的数组
$methods = get_class_methods(classname);
//返回类中属性的数组
$properties = get_class_vars(classname);

$class =
$methods = get_class_methods($class);
$methods = get_class_methods(Person);//same
$methods = get_class_methods("Person");
// same
```

PS:**get_class_vars()**只能得到有默认值以及在当前域可访问的属性。

###得到父类
```php
get_parent_class(classname);
```

##对象检查

```php
$is_object = is_object(var);
$classname = get_class(object);
//在执行方法之前，判断方法是否存在
$methodExists = method_exists(object, method);
//返回设置默认值的属性
get_class_vars()
//返回设置了值的属性
$array = get_object_vars(object);
```

##序列化（Serialization）
```php
$encoded = serialize(something);
$something = unserialize(encoded);
```



#Nginx的模块与工作原理