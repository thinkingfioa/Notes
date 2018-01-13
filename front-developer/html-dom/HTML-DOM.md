# HTML-DOM
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习html的网址是：http://www.runoob.com/htmldom/htmldom-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/ajax
```
---

## 1. HTML-DOM 教程
HTML DOM定义访问和操作HTML文档的标准方法，DOM以树结构表达HTML文档：
![HTML DOM树形结构](http://www.runoob.com/images/htmltree.gif)

## 2.HTML-DOM 简介
HTML-DOM定义了所有HTML元素的对象和属性，以及访问它们的方法，HTML-DOM是：

- 1.HTML的标准对象模型
- 2.HTML的标准编程接口
- 3.W3C标准

## 3. HTML-DOM节点
在HTML-DOM中，所有事物都是节点。DOM被视为节点树的HTML。

### 3.1 DOM节点
根据W3C的HTML DOM标准，HTML文档中的所有内容都是节点:

- 1.整个文档是一个文档节点
- 2.每个HTML元素是元素节点
- 3.HTML元素内的文本是文本节点，如:\<img...>链接\</img>元素中，链接就是一个文本节点
- 4.整个HTML属性是属性节点
- 5.注释是注释节点

### 3.2 HTML-DOM 节点树
HTML-DOM将HTML文档视作树结构。这种结构被称为节点树：
![HTML-DOM树实例](http://www.runoob.com/wp-content/uploads/2013/09/ct_htmltree.gif)

### 3.3 节点父、子和同胞
对于节点树，常用父(parent)、子(child)和同胞(sibling)等术语来描述这些关系。父节点拥有子节点，同级的子节点被称为同胞。

- 1.在节点树中，顶端节点被称为根(root)
- 2.每个节点都有父节点、除了根
- 3.一个节点可以拥有任意数量的子节点
- 4.同胞节点拥有相同的父节点。

如下图，展示了节点树的一部分，以及节点之间的关系：
![节点树](http://www.runoob.com/wp-content/uploads/2013/09/dom_navigate.gif)

## 4 HTML-DOM方法
- 1.HTML-DOM 方法是我们可以在节点(HTML元素)上执行的动作
- 2.HTML-DOM 属性是我们可以在节点(HTML元素)上设置和修改的值

### 4.1 编程接口
- 1.可通过JavaScript(以及其他编程语言)对HTML-DOM进行访问
- 2.所有的HTML元素都被定义为对象，而编程接口则是对象方法和对象属性
- 3.方法是能够执行的动作(比如添加或修改元素)
- 4.属性是能偶获取或设置的值(比如节点的名称或内容)

### 4.2 HTML-DOM对象的方法和属性
一些常用的HTML-DOM方法:

- 1.getElementById(id) - 获取带有指定id的节点(元素)
- 2.appendChild(node) - 插入新的子节点(元素)
- 3.removeChild(node) - 删除子节点(元素)

一些常用的HTML-DOM属性:

- 1.innerHTML - 节点(元素)的文本值
- 2.parentNode - 节点(元素)的父节点
- 3.childNodes - 节点(元素)的子节点
- 4.attributes - 节点(元素)的属性节点

### 4.3 HTML-DOM常用的对象方法
|方法|描述|
|:---|:---|
|getElementById()|返回带有指定ID的元素|
|getElementsByTagName()|返回包含带有指定标签名称的所有元素的节点列表|
|getElementsByClassName()|返回包含带有指定类名的所有元素的节点列表|
|appendChild()|把新的子节点添加到指定节点|
|removeChild()|删除子节点|
|replaceChild()|替换子节点|
|insertBefore()|在指定的子节点前面插入新的子节点|
|createAttribute()|创建属性节点|
|createElement()|创建元素节点|
|createTextNode()|创建文本节点|
|getAttribute()|返回指定的属性值|
|setAttribute()|把指定属性设置或修改指定的值|

## 5 HTML-DOM 属性
属性是节点(HTML元素)的值，能够获取或设置

### 5.1 编程接口
- 1.可通过JavaScript(以及其他编程语言)对HTML-DOM进行访问
- 2.所有的HTML元素都被定义为对象，而编程接口则是对象方法和对象属性
- 3.方法是能够执行的动作(比如添加或修改元素)
- 4.属性是能偶获取或设置的值(比如节点的名称或内容)

### 5.2 innerHTML 属性
获取元素内容的最简单方法是使用innerHTML属性
##### 代码:
```html
<body>
	<div>
		<p id = "demo">Hello World!</p>
	</div>
	<script>
		var text = document.getElementById("demo").innerHTML;
		document.write(text);
	</script>
</body>
```

### 5.3 nodeName属性
nodeName属性对于不同的节点呈现不同的含义，nodeName属性规定节点的名称:

- 1.nodeName是只读的
- 2.元素节点的nodeName与标签相同
- 3.属性节点的nodeName与属性名相同
- 4.文本节点的nodeName始终是#text
- 5.文档节点的nodeName始终是#document

### 5.4 nodeValue属性
nodeValue属性规定节点的值

- 1.元素节点的nodeValue是undefined或null
- 2.文本节点的nodeValue是文本本身
- 3.属性节点的nodeValue是属性值

#####  代码:
```html
<body>
	<div>
		<p id = "demo">Hello World!</p>
	</div>
	<script>
		var x = document.getElementById("demo");
		document.write(x.firstChild.nodeValue);
	</script>
</body>
```

### 5.5 nodeType属性
nodeType属性返回节点的类型，nodeType是只读的

|元素类型|NodeType|
|:---|:---|
|元素|1|
|属性|2|
|文本|3|
|注释|8|
|文档|9|

## 6 HTML-DOM访问
访问HTML元素等同于访问节点，提供三种不同的方式访问HTML元素

- 1.使用getElementById()方法
- 2.使用getElementsByTagName()方法
- 3.使用getElementsByClassName()方法

### 6.1 getElementById()方法
```html
<body>
	<div>
		<p id = "demo">Hello World!</p>
	</div>
	<script>
		var text = document.getElementById("demo").innerHTML;
		document.write(text);
	</script>
</body>
```

### 6.2 getElementsByTagName()方法
```html
<body>
	<div id="ppp">
		<p id = "demo">Hello World!</p>
		<p>Hello LWL</p>
	</div>
	<script>
		var xx = document.getElementById("ppp").getElementsByTagName("p");
		document.write(xx[1].firstChild.nodeValue);
	</script>
</body>
```

### 6.3 getElementsByClassName()方法
查找相同类名的所有HTML元素：document.getElementsByClassName("className");

## 7 HTML-DOM 修改
修改HTML = 改变元素、属性、样式和事件

### 7.1 修改HTML元素
- 1.改变HTML内容
- 2.改变CSS样式
- 3.改变HTML属性
- 4.创建新的HTML元素
- 5.删除已有的HTML元素
- 6.改变事件

### 7.2 改变HTML内容
改变元素内容最简单的方法是使用innerHTML属性，如:document.getElementById("p1").innerHTML="新文本";

### 7.3 改变HTML样式
通过HTML-DOM可以改变样式
##### 代码:
```html
<body>
	<p id="p1"> Hello LWL</p>
	<p id="p2"> Hello PPP</p>

	<script>
		document.getElementById("p2").style.color="green";
		document.getElementById("p2").style.fontFamily="Arial";
		document.getElementById("p2").style.fontSize="larger";
	</script>
</body>
```

### 7.3 创建新的HTML元素
先使用方法createElement创建该元素节点，然后追加到节点树中
##### 代码:
```html
<body>
	<div id="myDiv">
		<p id="p1"> Hello LWL</p>
		<p id="p2"> Hello PPP</p>
	</div>
	
	<script>
		var txtNode = document.createElement("p");
		txtNode.appendChild(document.createTextNode("Hello Thinking"));
		document.getElementById("myDiv").appendChild(txtNode);
	</script>
</body>
```

## 8 HTML-DOM 元素
添加、删除和替换HTML元素

### 8.1 创建新的HTML元素-createElement()
如果想向HTML DOM添加新元素，先创建该元素，然后将它追加到已有的元素
##### 代码:
```html
<body>
	<div id="myDiv">
		<p id="p1">You</p>
		<p id="p2">am</p>
	</div>
	<script>
		var newElement = document.createElement("p");
		newElement.appendChild(document.createTextNode("me"));
		document.getElementById("myDiv").appendChild(newElement);
	</script>
</body>
```

### 8.2 创建新的HTML元素-insertBefore()
appendChild()方法将元素添加到父元素末尾节点，如果希望将元素插入指定位置，使用insertBefore()方法
##### 代码:
```html
<body>
	<div id="myDiv">
		<p id="p1">I</p>
		<p id="p3">you too</p>
	</div>
	<script>
		var newElement = document.createElement("p");
		newElement.appendChild(document.createTextNode("am"));
		document.getElementById("myDiv").insertBefore(newElement, document.getElementById("p3"));
	</script>
</body>
```

### 8.3 删除已有的HTML元素-removeChild()
HTML中删除某个元素
##### 代码:
```html
<script>
	var parent=document.getElementById("div1");
	var child=document.getElementById("p1");
	parent.removeChild(child);
</script>
```

### 8.4 替换HTML元素-replaceChild()
##### 代码:
```html
<body>
	<div id="myDiv">
		<p id="p1">someOne</p>
		<p id="p2">like</p>
		<p id="p3">you</p>
	</div>
	<script>
		var parent = document.getElementById("myDiv");
		var newElement = document.createElement("p");
		node.appendChild(document.createTextNode("I"));
		var oldElement = document.getElementById("p1");
		parent.replaceChild(newElement, oldElement);
	</script>
</body>
```

## 9 HTML-DOM 事件
当事件发生时，可以执行JavaScript，达到对事件的处理，HTML事件的例子:

- 1.当用户点击鼠标时
- 2.当网页已加载时
- 3.当图片已加载时
- 4.当鼠标移动到元素上时
- 5.当输入字段被改变时
- 6.当HTML表单被提交时
- 7.当用户触发按键时


### 9.1 点击事件
点击文字，转换文字
##### 代码:
```html
<body>
	<h1 onclick="changeWords(this)" id="MyWords">点击文字</h1>
	<script>
		function changeWords(id) {
			id.innerHTML="Hello World!";
		}
	</script>
</body>
```

### 9.2 使用HTML-DOM来分配事件
使用javaScript向HTML元素分配事件,下列代码中，将函数displayDate()分配给id="MyButton"按钮
##### 代码:
```html
<body>
	<div>
		<button id="MyButton">点我</button>
	</div>
	<p id="myP1"></p>
	<script>
		document.getElementById("MyButton").onclick=function() {
			displayDate();
		}
		function displayDate() {
			document.getElementById("myP1").innerHTML=Date();
		}
	</script>
</body>
```

### 9.3 onload和onunload事件
当用户进入或离开页面时，会触发onload和onunload事件。可以使用onload事件检查访客浏览器版本等。
#####代码:
```html
<body onload="checkCookies()">
	<script>
		function checkCookies() {
			if(navigator.cookieEnabled == true){
				window.alert("Cookie 可用");
			} else {
				window.alert("Cookie 不可用");
			}
		}
	</script>
</body>
```

### 9.4 onchange事件
onchange事件常用于输入字段的验证，如下列代码将小写转大些
##### 代码:
```html
<body>
	<div>
		<span>小写字母变大写:</span>
		<input type="text" id="myText" name="someKey" onchange="myChange(this)">
	</div>
	<script>
		function myChange(txt) {
			txt.value= txt.value.toUpperCase();
		}
	</script>
</body>
```

### 9.5 onmouseover事件和onmouseout事件
onmouseover和onmouseout事件用于鼠标移动到或离开元素时触发函数
##### 代码:
```html
<body>
	<div onmousemove="mOver(this)" onmouseout="mOut(this)" style="background-color: #D94A38;width:150px;height: 20px; padding: 50px">
		<span>Mourse Over Me.</span>
	</div>
	<script>
		function mOver(obj) {
			obj.innerHTML="Thank You";
		}
		function mOut(obj) {
			obj.innerHTML="Mourse Over Me.";
		}
	</script>
</body>
```

### 9.6 onmousedown、onmouseup以及onclick事件
onmousedown、onmouseup和onclick事件是鼠标点击的全部过程。当鼠标按住时，触发onmousedown事件，鼠标被松开后，触发onmouseup事件。最后点击完成，触发onclick事件
##### 代码:
```html
<body>
	<p>onmousedown、onmouseup事件:</p>
	<div onmousedown="mDown(this)" onmouseup="mUp(this)" style="background-color: #D94A38;width:150px;height: 20px; padding: 50px">
		<span>按住我</span>
	</div>
	<script>
		function mDown(obj) {
			obj.style.backgroundColor="#1ec5e5";
			obj.innerHTML="请松开好嘛?"
		}
		function mUp(obj) {
			obj.style.backgroundColor="#D94A38";
			obj.innerHTML="按住我."
		}
	</script>
</body>
```
## 10 HTML-DOM 导航






































