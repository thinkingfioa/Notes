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
JavaScript有多种数据类型: 数字(Number)、字符串(String)、布尔(boolean)、对象(Object)和function。JavaScript对象其实就是键值对

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
字符串(String)、数字(Number)、布尔(Boolean)、对象(Object)、空(Null)、未定义(Undefined)。其中对象(Object)多数情况下就是键值对

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

## 10 JavaScript作用域
在JavaScript中，作用域为可访问变量、对象和函数的集合

### 10.1 JavaScript局部作用域
- 1.变量在函数内声明，只能在函数内使用，函数执行完后，局部变量自动销毁
- 2.函数参数也是局部变量，只能局部作用域。

### 10.2 JavaScript全局变量
- 1.变量定义在函数外，即为全局变量。全局作用域：网页中所有脚本和函数均可以使用
- 2.函数内，变量没有声明(没有使用var关键字),则认为该变量是全局变量

##### 代码:
```html
<script>
	var carName="Volvo";  // 全局变量
	myFunction();
	function myFunction(){
		// carName="BMW"; //全局变量
		document.getElementById("demo").innerHTML="显示变量carName: "+ carName;
	}
</script>
```

### 10.3 JavaScript变量生命周期
- 1.JavaScript变量生命周期在它声明时初始化
- 2.局部变量在函数执行完后销毁
- 3.全局变量在页面关闭后销毁

### 10.4 window对象
在HTML中，全局变量是window对象，所有的数据变量都属于window对象。

## 11 JavaScript事件
HTML事件是发生在HTML元素上的事情。

### 11.1 HTML事件
HTML事件可以是浏览器行为，也可以是用户行为。当事件发生时，可以执行一些JavaScript代码。HTML事件的实例有:

- 1.HTML页面完成加载
- 2.HTML input字段改变时
- 3.HTML的按钮被点击

### 11.2 常见的HTML事件
|事件|描述|
|:---:|:---:|
|onchange|HTML元素改变|
|onclick|用户点击HTML元素|
|onmouseover|用户在一个HTML元素上移动鼠标|
|onmouseout|用户从一个HTML元素上移开鼠标|
|onkeydown|用户按下键盘按键|
|onload|浏览器完成页面的加载|

##### 代码:
```html
<body>
	<div>
		<span>HTML事件中onchange事件</span>
	</div>
	<input type="text" name="me" value="thinking" onchange="onChange(this)">

	<script>
		function onChange(cc){
			window.alert("文本改为: "+ cc.value);
		}
	</script>
</body>
```

## 12 JavaScript字符串
- 1.JavaScript字符串用于存储和处理文本
- 2.字符串的索引从0开始，依次类推。类似于其他语言
- 3.如果把数字与字符串相加，结果将变成字符串

### 12.1 字符串长度
使用内置属性length来计算字符串长度，如: var strSize=str.length;

### 12.2 字符串可以对象
- 1.var firstName="thinking"，其是一个字符串
- 2.var firstName=new String("thinking")，其是一个Object 对象

### 12.3 JavaScript中==与===区别
- 1.对于string、number等基础类型，==只会比价值是否相等，===不仅要求值相等还要求数据类型相同
- 2.对于Array、Object等高级类型，没有区别，进行指针地址比较
- 3.!=是==的非运算，!==是===的非运算

##### 代码:
```html
<script>
	var firstName="thinking";
	var firstName2=new String("thinking");
	console.log(typeof firstName); //输出: string
	console.log(typeof firstName2); //输出: object
	console.log(firstName == firstName2); //输出: true
	console.log(firstName === firstName2); //输出: false
</script>
```

### 12.4 字符串方法
字符串方法，请看[地址](http://www.runoob.com/jsref/jsref-obj-string.html)

## 13 JavaScript条件语句语法
```html
if(time<10){
	//some thing
} else if(time>10 && time <20){
	//some thing
} else {
	//some thing
}
```

## 14 JavaScript switch语句语法
```html
switch(d){
	case 1: code line;
		break;
	case 2: code line;
		break;
	default:
		break;
}
```

## 15 JavaScript循环
- 1.for循环
- 2.for/in循环, 比如: for(onePerson : persons){...}
- 3.while循环
- 4.do/while循环
- 5.break/continue与其他语言一样

## 16 JavaScript中typeof、null、undefined和valueOf()
- 1.string、number、boolean等基础类型，typeof会得到对应的类型
- 2.array、object、Date、null等高级类型，typeof会得到Object类型
- 3.所有利用关键字new得到的变量，都是object数据类型变量。在进行==或===比较时，要注意

### 16.1 null和undefined区别
- 1.通常设置对象为null，来清空对象
- 2.undefined的类型是undefined，null的类型是object。null==undefined返回true; null===undefined返回false

##### 代码:
```html
<script>
	console.log(typeof undefined); //输出: undefined
	console.log(typeof null); //输出: object
	console.log(null == undefined); //输出: true
	console.log(null === undefined); //输出: false
</script>
```

## 17 JavaScript类型转换
- 1.在JavaScript中有5种不同的数据类型:
 - string
 - number
 - boolean
 - object
 - function
- 2.3种对象类型:
 - Object
 - Date
 - Array
- 3.2种不包含任何值的数据类型
 - null
 - undefined

### 17.1 typeof操作符
```html
<script>
	console.log(typeof "thinking"); //输出: string
	console.log(typeof 3.1415); //输出: number
	console.log(typeof new String("fioa")); //输出: object
	console.log(typeof [1,2,3]); //输出: object 
	console.log(typeof {name:"ppp", age:18}); //输出: object
	console.log(typeof function(){}); //输出: function
	console.log(typeof null); //输出: object
	console.log(typeof undefined); //输出: undefined
</script>
```

### 17.2 constructor属性
constructor属性返回所有JavaScript变量的构造函数，可以被用来判断类型

##### 代码:
```html
isNumber(321);
function isNumber(num){
	console.log("isNumber:" + ((num).constructor.toString().indexOf("Number") > -1));
}
```

### 17.3 JavaScript类型转换
- 1.全局方法String()可以将数字、布尔和日期转换成字符串。或者是toString()方法
- 2.全局方法Number()可以将字符串、布尔和日期转换成数字。若无法转换，则变为NaN
- 3.一元运算符+，可以将变量转化为数字。如:var x= + "5";

### 17.4 typeof用来判空
- 1.判断某个变量是否存在，请不要使用if(a)。替换为:if(typeof a!="undefined"){}
- 2.使用关键字instanceof来判断对象类型。如: if(arr instanceof Array){} 、

## 18 JavaScript正则表达式
- 1.语法: /正则表达式主体/修饰符(可选)。如: /runooob/i中runoob是一个正则表达式主体(用于检索),i是一个修饰符(检索不区分大小写)
- 2.正则表达式可参考[地址](http://www.runoob.com/js/js-regexp.html)

### 18.1 正则表达式两个字符串方法
- 1.search()用于检索指定的子字符串，返回子串的起始位置
- 2.replace()用于替换字符串中特定的子串

##### 代码:
```html
<script>
	function ClickButton(name){
		var str = document.getElementById("demo").innerHTML;
		var txt = str.replace(/microsoft/i, name)
		document.getElementById("demo").innerHTML=txt;
	}
</script>
```

## 19 JavaScript错误-throw、try和catch
try-catch基本和Java保持一致
##### 代码:
```html
<script>
		function tryCatchFunction() {
		try {
			if(x<0) throw "不能为负数";
			.....
		}catch(err) {
			alert(err);
			some.innerHTML=err.message;
		}
	}
</script>
```

## 20 JavaScript变量提升
- 1.在JavaScript中，函数及变量的声明都会被提升到函数的最顶部，所以变量可以先使用后声明，但不推荐这样
- 2.只有函数和变量的声明会提升到最顶部，**初始化则不会**，请注意

## 21 JavaScript表单
HTML表单验证可以使用JavaScript来完成。下面代码验证必须填写字段

##### 代码：
```html
<body>
	<form name="myForm" action="some.php" onsubmit="return myFunction()" method="post">
		<span>名字:</span>
		<input type="text" name="myText">
		<input type="submit" value="提交">
	</form>
	<script> 
		function myFunction(){
			var txt = document.forms["myForm"]["myText"].value;
			if(txt == null || txt ==""){
				window.alert("必填");
				return false;
			}
		}
	</script>
</body>
```

## 22 JavaScript验证API
提供属性min或属性max，可以约束type="number"最小值和最大值范围，提供特定API进行验证

## 23 JavaScript JSON
JavaScript提供方法与JSON格式的数据交互。

### 23.1 JSON.parse()
JSON.parse()方法用于将一个JSON格式的数据转换为JavaScript对象
##### 代码:
```html
<body>
	<div>
		<h3>为JSON字符串创建对象
	</div>
	<p id="demo"></p>
	<script>
		var txt = '{ "sites" : [' +
			'{ "name":"Runoob" , "url":"www.runoob.com" },' +
			'{ "name":"Google" , "url":"www.google.com" },' +
			'{ "name":"Taobao" , "url":"www.taobao.com" } ]}';

		var obj = JSON.parse(txt);
		document.getElementById("demo").innerHTML=obj.sites[1].name + " " + obj.sites[1].url;
	</script>
</body>
```

### 23.2 JSON.stringify()
JSON.stringify()方法用于将JavaScript值转化为JSON字符串
##### 代码:
```html
<script>
	var txt = JSON.stringify(obj);
</script>
```

## 24 JavaScript void
void是JavaScript中非常重要的关键字，该操字符指定要计算一个表达式但是不返回值

### 24.1 语法格式
```html
<script>
	void(func())
	javascript:void(func()) // 比如: javascript:void(alert('Warning!')
</script>
```

### 24.2 javascript:void(0)含义
javascript:void(0)常被用不做任何事情。





















