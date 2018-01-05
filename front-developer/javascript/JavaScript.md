# JavaScript学习
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习javaScript的网址是：http://www.runoob.com/js/js-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/javascript
```
---

## 1. JavaScript简介

### 1.1 JavaScript脚本语言
- 1. JavaScript可插入HTML页面的编程代码
- 2. JavaScript是一种轻量级编程语言
- 3. JavaScript字母大小写敏感
- 4. JavaScript是解释形脚本语言，浏览器会逐行执行脚本代码

### 1.2 学习JavaScript内容介绍
- 1. JavaScript：直接写入HTML输出流
- 2. JavaScript：对事件的反应
- 3. JavaScript：改变HTML内容
- 4. JavaScript：改变HTML图像
- 5. JavaScript：改变HTML样式
- 6. JavaScript：验证输入

## 2. JavaScript用法
HTML中的脚本必须位于\<script>和\</script>标签之间。标本可以被放置在HTML页面的\<body>和\<head>部分中。

### 2.1 JavaScript函数和事件
当某个事件发生时执行代码，比如用户点击按钮。所以，我们将代码放在函数中，当事件发生时，调用该函数。

### 2.2 在\<head>或者\<body>中的JavaScript
- 1. 通常脚本可以位于\<head>或\<body>中，两个都有也可以
- 2. 喜欢将脚本函数放入\<head>中，或者页面的底部。保证不干扰页面的内容

### 2.3 外部的JavaScript
可以将脚本保存到多个外部文件中，改文件被多个网页使用

##### 代码:
```
<body>
	<script src="myJavaScript.js"></script>
</body>
```

## 3 JavaScript输出
JavaScript没有任何打印或者输出函数。

### 3.1 JavaScript显示数据
- 1. 使用window.alert("hello world")弹出警告框
- 2. 使用document.write("\<h1>hello thinking\</h1>")方法将内容写到HTML文件中
- 3. 使用innerHTML元素，写在HTML某个属性中
- 4. 使用console.log("hello ppp");写到浏览器的控制台

##### 代码:
```html
<body>
	<p id="demo">需要变化</p>
	<script>
		function alertFunction(){
			window.alert("hello world");
		}
		function alertDocument(){
			document.write("hello thinking");
		}
		function alertInnerHTML(){
			document.getElementById("demo").innerHTML="hello ppp";
		}
		function alertConsole(){
			console.log("hello fioa");
		}
	</script>

	<input type="button" value="Alert" onclick="alertFunction()">
	<input type="button" value="Document" onclick="alertDocument()">
	<input type="button" value="InnerHTML" onclick="alertInnerHTML()">
	<input type="button" value="Console" onclick="alertConsole()">
</body>
```

## 4 JavaScript语法
JavaScript是一个脚本语言，轻量级。JavaScript语言注释使用双斜杠: //

### 4.1 JavaScript变量
在编程语言中，变量用来存储数据值。JavaScript使用关键字var来定义变量，等号来赋值。

### 4.2 JavaScript数据类型
JavaScript有多种数据类型: 数字、字符串、数组和对象等。JavaScript对象其实就是键值对

##### 代码:
```html
var length = 16;
var lastName = "fioa";
var cars=["BMW","Volvo","BenZ"];
var person={firstName:"thinking", lastName="fioa"};
```

## 5 JavaScript语句
JavaScript语句想浏览器发出命令，告诉浏览器该如何做

## 6 JavaScript变量
- 1.如果JavaScript变量未初始化，缺省值为: undefined
- 2.重新声明JavaScript变量，该变量的值不会丢失。如: var name="Volvo"; var name;

## 7 JavaScript数据类型
字符串(String)、数字(Number)、布尔(Boolean)、数组(Array)、对象(Object)、空(Null)、未定义(Undefined)。其中对象(Object)就是键值对

### 7.1 JavaScript拥有动态类型
JavaScript拥有动态的类型，意味着相同的变量可被用作不同的类型
##### 代码：
```html
var x;
var x=3.1415;
var x="fioa";
```

### 7.2 JavaScript基本数据类型解释
- 1.JavaScript字符串：使用单引号或双引号。
- 2.JavaScript数字：小数、整数和科学计数法。如: var y=123e5
- 3.JavaScript布尔: 布尔只有两个值：true或false
- 4.JavaScript中Undefined和Null：Undefined表示该变量不含有值。null常被用来清空变量。

### 7.3 JavaScript数组
创建JavaScript数组有三种方式:

- 1.直接赋值方式：var cars=["Saab","Volvo","BMW"]
- 2.使用new关键字: var cars=new Array("Saab","Volvo","BMW");
- 3.使用new关键字后再赋值：var cars=new Array();cars[0]="Saab";cars[1]="Volvo";

### 7.4 JavaScript对象
JavaScript中的对象就是键值对，有下列代码可参考:
##### 代码：
```html
var persons={firstname:"thinking", lastname:"fioa", age:18};
或：
var persons={
	firstname:"thinking", 
	lastname:"fioa", 
	age:18
};
调用方式:
var name=persons.firstname;
var name=persons[firstname];
``` 

## 8 JavaScript对象
JavaScript对象是拥有属性和方法的容器

### 8.1 对象属性
通常JavaScript对象是键值对的容器，类似于Python中的字典

### 8.2 对象的方法
可以在对象中定义一个函数，创建对象方法语法: methodName : function() {...}
##### 代码:
```html
var person={
	firstname="thinking",
	lastname="fioa",
	getName : function(){
		return this.firstname+"_"+this.lastname;
	}
};
```

## 9 JavaScript函数
JavaScript函数和对象方法不同，无论是语法还说调用。其实通俗的说一个是面向方法编程，一个是面向对象编程。

### 9.1 JavaScript函数语法
```html
function myFunction {
	code lines...
}
```

### 9.2 调用带参数的函数
- 1.调用函数时，可以传递参数。
- 2.变量和参数**必须**以一致的顺序出现。第一个变量就是被传递给函数第一个参数

##### 代码：
```html
<body>
	<div>
		<span>点击这个按钮，来调用带参数的函数。</span>
	</div>
	<button onclick="myFunction('thinking', 'ppp')">点击这里</button>
	<script>
		function myFunction( name, job) {
			window.alert("Welcome "+name+", the "+job);
		}
	</script>
</body>
```

### 9.3 带有返回值的函数语法
```html
function calFunction(a, b){
	return a+b;
}
```

### 9.4 局部JavaScript变量
在JavaScript函数内部声明的变量(使用var)是局部变量，只能当前函数内部可以访问，函数执行完毕，局部变量被删除。

### 9.5 全局JavaScript变量
在函数外声明的变量是全局变量，网页上所有的脚本和函数都可以访问。

### 9.6 JavaScript变量的生存周期
JavaScript变量的生命周期是从它们声明的时间开始。局部变量会在函数运行结束后被删除，全局变量会在页面关闭后被删除。

### 9.7 向未声明的JavaScript变量分配值
如果把值赋值给未声明的变量，该变量会被自动作为全局变量声明。如: carname="Volvo"，那么carname变成了全局变量，即使在函数内也会变成全局变量。





























