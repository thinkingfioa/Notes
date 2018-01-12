# AJAX
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习html的网址是：http://www.runoob.com/ajax/ajax-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/ajax
```
---

## 1 AJAX教程
- 1.AJAX=Asynchronous JavaScript And XML(异步的JavaScript和XML)
- 2.AJAX不是新的编程语言，而是一种使用现有标准的新方法
- 3.AJAX最大的优点是不重新加载整个页面的情况下，可以与服务器交换数据并更新网页部分内容

### 1.1 AJAX应用
- 1.运用XHTML+CSS来表达资讯
- 2.运用JavaScript操作DOM(Document Object Model)来执行动态效果
- 3.运用XML和XSLT操作资料
- 4.运用XMLHttpRequest或新的Fetch API与网页服务器进行一步资料交换
- 5.注意：AJAX与Flash、Silverlight和Java Applet等RIA技术是有区分的

## 2 AJAX 简介
AJAX是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术

### 2.1 AJAX是基于现有的Internet标准
AJAX是基于现有的Internet标准，并且联合使用它们:

- 1.XMLHttpRequest对象(异步的与服务器交换数据)
- 2.JavaScript/DOM（信息显示／交互)
- 3.CSS(定义数据样式)
- 4.XML(作为转换数据的格式)

## 3 AJAX的DEMO
DEMO主要完成的任务是：点击一个按钮，向服务器请求数据，再显示出来
##### 代码:
```html
<body>
	<div>
		<h2 id="demo">使用AJAX修改该文本内容</h2>
	</div>
	<button id="myButton" onclick="loadXMLDoc()">修改内容</button>

	<script>
		function loadXMLDoc() {
			var xmlhttp;
			if(window.XMLHttpRequest) {
				//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
				xmlhttp = new XMLHttpRequest();
			} else {
				// IE6, IE5 浏览器执行代码
				xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
			}
			xmlhttp.onreadystatechange=function() {
				if(xmlhttp.readyState=-4 && xmlhttp.status == 200) {
					document.getElementById("demo").innerHTML=xmlhttp.responseText;
				}
			}
			xmlhttp.open("GET", "some_url.php", true);
			xmlhttp.send();
		}
	</script>
</body>
```

## 4 AJAX - 创建XMLHttpRequest对象
XMLHttpRequest对象用于后台与服务器交换数据，所有现在浏览器均支持XMLHttpRequest对象(IE5盒IE6使用ActiveXObject)，具体细节可以看上面的代码。

## 5 AJAX - 向服务器发送请求
使用XMLHttpRequest对象的open()和send()方法。

### 5.1 open方法
open(method, url, async)方法规定请求类型、URL和是否异步处理请求。method类型就是GET或POST。async：true(异步)或false(同步)

### 5.2 send方法
send(string)将请求发送到服务器。其中如果请求类型为post时，string才可以使用

### 5.3 GET请求
```html
xmlhttp.open("GET", "some_get.php?name="+userName, true);
xmlhttp.send();
```

### 5.4 POST请求
```html
xmlhttp.open("POST","some_post.php", true);
xmlhttp.send("name=usreName&password=pw");
```

## 6 AJAX - 服务器响应
XMLHttpRequest对象提供responseText或responseXML属性，来获得服务器返回的数据

|属性|描述|
|:---:|:---:|
|responseText|获得字符串形式的响应数据|
|responseXML|获得XML形式的响应数据|











