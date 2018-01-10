# HTML5
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习html的网址是：http://www.runoob.com/html/html5-intro.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/html5
```
---

## 1 HTML5特性
HTML5中的一些有趣的新特性:

- 1.用于绘画的canvas元素
- 2.用于媒介回放的video和audio元素
- 3.对本地离线存储提供更好的支持
- 4.新的特殊内容元素,如:article、footer、heaader、nav、selection
- 5.新的表单控件，如:calendar、date、time、email、url、search

## 2 HTML5 Canvas
HTML5\<canvas>元素用于图形的绘制，提供图形容器，通过脚本(通常是JavaScript)来绘制图形

### 2.1 创建一个画布(Canvas) 
一个画布在网页中是一个矩形框，通过\<canvas>元素来绘制。

##### 代码:
```html
<body>
	<canvas id="myCanvas" width="200px" height="100px" style="border: 1px solid #000000;">
		浏览器不支持Canvas标签
	</canvas>
</body>
```

### 2.2 使用JavaScript来绘制图像
canvas元素本身没有绘图能力，所有的绘制工作由JavaScript内部完成

##### 代码:
```html
<canvas id="myCanvas1" width="200px" height="100px" style="border: 1px solid #000000">
	浏览器不支持Canvas标签
</canvas>

<script>
	var c = document.getElementById("myCanvas1");
	var ctx = c.getContext("2d");
	ctx.fillStyle="#00FF00";
	ctx.fillRect(0,0,166,66);
</script>
```

### 2.3 Canvas坐标
canvas是一个二维网格，左上角坐标是(0,0)，横轴是x轴，竖轴是y轴。

### 2.4 Canvas-路径(线条)
在Canvas上画线，可以使用下列两种方法:

- 1.moveTo(x,y)定义线条开始坐标
- 2.lineTo(x,y)定义线条结束坐标

##### 代码:
```html
<script>
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");
	ctx.moveTo(0,0);
	ctx.lineTo(200,100);
	ctx.stroke(); 
</script>
```

### 2.5 Canvas-圆
Canvas可以画圆形，具体方法是: arc(x,y,r,start,stop)
##### 代码:
```html
<script>
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");
	ctx.beginPath();
	ctx.arc(95,50,40,0,2*Math.PI);
	ctx.stroke();
</script>
```

### 2.6 Canvas-文本
使用canvas绘制文本，重要的属性和方法如下:

- 1.font定义字体
- 2.fillText(text, x, y)在canvas上绘制实心的文本
- 3.strokeText(text, x, y)在canvas上绘制空心的文本

##### 代码:
```html
<script>
	var c = document.getElementId("myCanvas");
	var ctx = c.getContext("2d");
	ctx.font="30px Arial";
	ctx.fillText("Hello World", 10, 50);
</script>
```

### 2.7 Canvas-渐变
渐变可以填充在矩形、圆形、和文本等等。以下有两种不同的方式设置Canvas渐变:

- 1.createLinearCradient(x,y,x1,y1)创建线条渐变
- 2.createRadialGradient(x,y,r,x1,y1,r1)创建一个径向／圆渐变

当使用渐变对象时，必须使用两种或两种以上的停止颜色。addColorStop()方法指定颜色停止，参数使用坐标描述，可以是0或1.

##### 代码:
```html
// 线性变化
<script>
	var v5 = document.getElementById("myCanvas5");
	var ctx5 = v5.getContext("2d");
	// 创建渐变
	var grd = ctx5.createLinearGradient(0, 0, 200, 0);
	grd.addColorStop(0, "red");
	grd.addColorStop(1, "white");
	// 填充渐变
	ctx5.fillStyle=grd;
	ctx5.fillRect(10, 10, 150, 80);
</script>
//径向／圆渐变
<script>
	var v6 = document.getElementById("myCanvas6");
	var ctx6 = v6.getContext("2d");
	var grd6 = ctx6.createRadialGradient(75,50,5,90,60,50);
	grd6.addColorStop(0, "red");
	grd6.addColorStop(1,"white");
	ctx6.fillStyle=grd6;
	ctx6.fillRect(10,10,150,80);
</script>
```

### 2.8 Canvas-画像
将一幅图画放到画布上，使用以下方法:

- drawImage(image,x,y)

##### 代码:
```html
<body>
	<img id="myHeadPic" src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" width="230px" height="300px" alt="无法加载">
	<canvas id="myCanvas7" width="400px" height="350px" style="border: 1px solid #000000">
		浏览器不支持Canvas标签
	</canvas>
	<script>
		var v = document.getElementById("myCanvas7");
		var ctx = v.getContext("2d");
		var img = document.getElementById("myHeadPic");
		img.onload = function(){
			ctx.drawImage(img, 10,10);
		}
	</script>
</body>
```

## 3 HTML5内联SVG
HTML5支持内联SVG，SVG是使用XML格式定义图片。

## 4 HTML5 MathML
在HTML5中可以使用MathML元素，对应的标签是\<math>...\</math>。MathML是一个数学标记语言，是一种基于XML的标准，用来写网页版的数学符号和公式。

## 5 HTML5 拖放
### 5.1 设置元素为可拖放
为了是元素可拖动，把draggable属性设置为true,则：\<img draggable="true">

### 5.2 拖动什么-ondragstart和setData()
规定当元素被拖动时，会发生什么。ondragstart属性需要定义函数drag(event)，函数中需要填入拖动的数据。

### 5.3 放在何处-ondragover
ondragover事件规定在何处放置被拖动的数据

### 5.4 进行放置-ondrop
当放置被拖动数据时，会发生drop事件

##### 代码:
```html
<body>
	<div>
		<span><h3>拖动头像进入矩形框</h3></span>
	</div>
	<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)" style="width: 350px;height: 350px;padding: 10px;border: 1px solid #000000"></div>

	<br/>
	<img id="img1" src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" draggable="true" ondragstart="drag(event)" width="300px" height="300px">

	<script>
		function drag(ev) {
			ev.dataTransfer.setData("Text", ev.target.id);
		}
		function allowDrop(ev) {
			ev.preventDefault();
		}
		function drop(ev) {
			ev.preventDefault();
			var data = ev.dataTransfer.getData("Text");
			ev.target.appendChild(document.getElementById(data));
		}
	</script>
</body>
```

## 6 HTML5 地理定位
HTML5 Geolocation API用于获得用户的地理位置。该特性可能侵犯用户的隐私，HTML5可以做到

## 7 HTML5 Video(视频)
HTML5规定一种通过video元素来包含视频的标准方法，具体代码如下:

```html
<video widht="320px" height="320" controls>
	<source src="" type="video/mp4">
	<source src="" type="video/ogg">
</video>
```

## 8 HTML5 Audio(音频)
HTML5中规定音频元素标准，使用<audio>元素，具体代码如下:

```html
<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
</audio>
```

## 9 HTML5 Input类型
HTML5拥有多个新的表单输入类型，新的特性提供更好的输入控制和验证。新的输入类型：color、date、datetime、datetime-local、email、month、number、range、search、tel、time、url、week。

### 9.1 Input类型: color
color类型用在input字段主要用于从拾色器中选择颜色
##### 代码:
```html
<form action="some_url.html" method="get">
	<div>
		<span>选择你喜欢的颜色:</span>
	</div>
	<input type="color" name="favorite">
	<input type="submit" value="提交">
</form>
```

### 9.2 Input类型: date
date类型允许从日期选择器选择一个日期，代码:\<input type="date" name="bday">

### 9.3 Input类型: datetime-local
datetime-local类型允许你选择一个日期，但具体怎么用的，我没整明白

### 9.4 Input类型: email
email类型用于应该包含e-mail的地址输入域，会进行email格式的校验。如:\<input type="email" name="usremail">

### 9.5 Input类型: month
month类型允许选择年／月，时间精确到月份。如:\<input type="month" name="bdaymonth">

### 9.6 Input类型: number
number类型用于包含数值的输入域。该类型有较多的属性，请看下面的代码:
##### 代码:
```html
<form id="myForm" action="some_url.html" method="get">
	<input type="number" name="points" min="0" max="10" step="3" value="6">
	<input type="submit" value="提交表单">
</form>
```

### 9.7 Input类型: range
range类型的显示为滑动条，包括一定的范围。如: \<input type="range" name="myRange" min="1" max="10" step="2" value="4">。其中value属性是规定默认值

### 9.8 Input类型: search
search类型用于定义搜索域，比如站点搜索等。如:\<input type="search" name="mySearch">。完全是让好理解，我觉得文本框也可以做到。

### 9.9 Input类型: tel
定义输入电话号码，完全是让好理解，我觉得文本框也可以做到。如:\<input type="tel" name="myTel">

### 9.10 Input类型: time
time类型允许你选择一个时间，如:\<input type="time" name="usr_time"> 

### 9.11 Input类型: url
url类型包含URL地址输入域，在提交表单时，自动验证url域的值。如:\<input type="url" name="homepage">

### 9.12 Input类型: week
week类型允许选择周和年

## 10 HTML5表单元素
HTML5有以下新的表单元素:

- 1.\<datalist>
- 2.\<keygen>
- 3.\<output>

### 10.1 HTML5 \<datalist>元素
\<datalist>元素规定输入域的选择列表，但是如果用户自己输入，也可以。
##### 代码:
```html
<form action="some_url.html" method="get">
	<input list="girlfriends" name="girlfriends">
	<datalist id="girlfriends">
		<option value="PPP1"></option>
		<option value="PPP2"></option>
		<option value="PPP3"></option>
		<option value="PPP4"></option>
		<option value="PPP5"></option>
	</datalist>
	<input type="submit" value="提交">
</form>
```

### 10.2 HTML5\<keygen>元素
\<keygen>标签规定用于表单的密钥对生成器，我没有理解怎么用？请补充实例?
##### 代码:
```html
```

### 10.3 HTML5\<output>元素
\<output>元素用于不同类型的输出，比如计算或脚本输出：
##### 代码:
```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">
	<div>
		<sapn>0</sapn>
		<input type="range" id="a" value="50">
		<span>100+</span>
		<input type="number" id="b" value="50">
		<span>=</span>
		<output name="x" for="a b"></output>
	</div>
</form>
```

## 11 HTML5表单属性
HTML的\<form>和\<input>标签新加了几个属性
\<form>的新属性:

- 1.autocomplete
- 2.novalidate

\<input>的新属性:

- 1.autocomplete
- 2.autofocus
- 3.form
- 4.formaction
- 5.formenctype
- 6.formmethod
- 7.formnovalidate
- 8.formtarget
- 9.height 与 width
- 10.list
- 11.min 与 max
- 12.multiple
- 13.pattern (regexp)
- 14.placeholder
- 15.required
- 16.step

### 11.1 \<form>和\<input> autocomplete属性
- 1.autocomplete属性规定form和input域应该拥有自动完成的功能。当用户在自动完成域中开始输入时，浏览器应该在该域中显示填写的选项。
- 2.autocomplete属性有可能在form元素中开启的，而是在input元素中关闭

##### 代码:
```html
<form action="some_url.php" method="get" autocomplete="on">
	<span>First name:</span>
	<input type="text" name="firstName"><br/>
	<span>Last Name:</span>
	<input type="text" name="lastName"><br/>
	<span>E-mail:</span>
	<input type="email" name="email" autocomplete="off"><br/>
	<input type="submit" value="submit">
</form>
```

### 11.2 \<form> novalidate 属性
novalidate属性是一个boolean属性。规定在提交表单时不应该验证form或input域

##### 代码:
```html
<form action="some_url.php" method="get" novalidate>
	<span>E-mail:</span>
	<input type="email" name="myEmail">
	<input type="submit" value="submit">
</form>
```

### 11.3 \<input> autofocus属性
autofocus属性是一个boolean属性，规定在页面加载时，域自动获得焦点
##### 代码:
```html
<form action="some_url.php" method="get" autofocus>
	<span>First Name:</span>
	<input type="text" name="firstName" >
	<span>Last Name:</span>
	<input type="text" name="lastName">
	<input type="submit" value="submit">
</form>
```

### 11.4 \<input> form属性
\<input>标签中有属性form，可以指明该标签属于哪个form表单，即使该标签不在其对应的form域内。比如: 例子中lastName标签不在id=form1表单中，但是提交按钮会一起打包提交。
##### 代码:
```html
<form id="form1" action="some_url.php" method="get"> 
	<span>First Name:</span>
	<input type="text" name="firstName">
	<input type="submit" value="submit">
</form>
<span>Last Name:</span>
<input type="text" name="lastName" form="form1">
```

### 11.5 \<input> formaction属性
formaction属性用于描述表单提交的URL地址，会覆盖\<form>元素中的action属性，\<form>元素中的action属性会无效
##### 代码:
```html
<form action="some_url.php" method="get" novalidate>
	<span>E-mail:</span>
	<input type="email" name="myEmail">
	<input type="submit" value="submit" formaction="your_ur.php">
</form>
```

### 11.6 \<input> formenctype属性
formenctype属性描述了表单提交到服务器的数据编码,只对form表单中method="post"有效。且会覆盖form元素中的enctype属性
##### 代码
```html
<form action="some_url.html" method="post">
	<span>PPP:</span>
	<input type="text" name="ppp">
	<input type="submit" value="提交" formenctype="multipart/form-data">
</form>
```

### 11.7 \<input> formmethod属性
formmethod属性定义了表单提交的方式，会覆盖form元素中的method属性，formmethod="post"

### 11.8 \<input> formnovalidate属性
novalidate属性是一个boolean属性，描述\<input>元素提交时无需验证。formnovalidate属性可实现同样的效果，**注意：**formnovalidate属性与type="submit"提起使用
##### 代码:
```html
<form action="some_url.php" method="post">
	<span>lwl-E-mail:</span>
	<input type="email" name="lwl-email">
	<input type="submit" value="提交" formnovalidate> 
</form>
```

### 11.9 \<input> formtarget属性
formtarget属性指定一个名称或一个关键字来指明表单提交数据接收后的展示。目前没有懂，下面的例子没什么用，运行结果一样的
##### 代码:
```html
<form action="demo-form.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="正常提交">
  <input type="submit" formtarget="_blank" value="提交到一个新的页面上">
</form>
```

### 11.10 \<input> height和width属性
height和width属性规定用于type="image"标签的图像大小。type="image"标签用于图片代替type="submit"提交按钮
##### 代码：
```html
<form action="some_url.php" method="get">
	<span>First name:</span>
	<input type="text" name="firstName"><br/>
	<span>Last Name:</span>
	<input type="text" name="lastName"><br/>
	<span>E-mail:</span>
	<input type="image" src="http://www.runoob.com/try/demo_source/img_submit.gif" alt="Submit" width="50" height="50">
</form>
```

### 11.11 \<input> list属性
list属性规定输入域为datalist。datalist输入域定义选项列表

##### 代码:
```html
<form action="some_url.php" method="get">
	<input list="browsers" name="browser">
	<datalist id="browsers">
		<option value="Internet Explorer"></option>
		<option value="Firefox"></option>
		<option value="Chrome"></option>
	</datalist>
	<input type="submit">
</form><br/>
```

### 11.12 \<input> min和max属性
min、max和step属性用于包含数字或日期的input类型的约束。适用于类型的\<input>标签: date picker、number和range。

### 11.13 \<input> multiple属性
multiple属性是一个boolean属性，规定\<input>元素中可选择多个值，使用于标签: email和file

##### 代码:
```html
<form action="some_url.php" action="get">
	<span>选择图片:</span>
	<input type="file" name="chooseFile" multiple>
	<input type="submit" value="提交">
</form>
```

### 11.14 \<input> pattern属性
- 1.pattern属性描述了一个正则表达式，用于验证\<input>元素的值。适用于一些类型标签: text、search、url、tel、email和password
- 2.使用title显示提示信息

##### 代码:
```html
<form action="some_url.php" method="get">
	<span>Country Code:</span>
	<input type="text" name="countryCode" pattern="[A-Za-z]{3}" title="请使用3个字母">
	<input type="submit" value="提交">
</form>
```

### 11.15 \<input> placeholder属性
placeholder属性提供一种提示(hint)，描述输入域所期待的值，适用于以下类型标签:text、search、url、telephone、email和password

##### 代码:
```html
<form action="some_url.php" method="get">
	<span>First Name:</span>
	<input type="text" name="fName" placeholder="thinking">
	<span>Last Name:</span>
	<input type="text" name="lName" placeholder="fioa">
	<br/>
	<input type="submit" value="Sumbit">
</form>
```

### 11.16 \<input> required属性
required属性是一个boolean属性。规定在提交之前必须填写输入域(不能为空)。适用的标签有: text、search、url、telephone、email、password、date pickers、number、checkbox、radio和file

##### 代码:
```html
<form action="some_url.php" method="get">
	<span>Username:</span>
	<input type="text" name="userName" required>
	<input type="submit" value="Submit">
</form>
```

### 11.17 \<input> step属性
step规定了合法的数字间隔，step属性往往和min、max属性创建一个区域值。适用的标签有:number、range、date、datetime、datetime-local、month、time和week.

## 12 HTML5 语义元素
语义元素指的是有意义的元素，能够清楚描述其意义给开发者。比如\<div>或\<span>就是无意义，而\<table>则是语义元素。

### 12.1 HTML5中新的语义元素
HTML5提供了新的语义元素来明确一个Web页面的不同部分:

- 1.\<header>
- 2.\<nav>
- 3.\<section>
- 4.\<article>
- 5.\<aside>
- 6.\<figcaption>
- 7.\<figure>
- 8.\<footer>

具体如图所示:![页面布局](http://img.blog.csdn.net/20180110152700551?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 12.2 HTML5 \<section>元素
\<section>标签定义文档中的节，包含一组内容及其标题

##### 代码:
```html
<body>
	<section>
		<h1>标题1</h1>
		<p>第一个段落</p>
	</section>
	<section>
		<h1>标题2</h1>
		<p>第二个段落</p>
	</section>
</body>
```

### 12.3 HTML5\<article>元素
\<article>标签定义独立的内容
##### 代码:
```html
<body>
	<article>
		<h1>Internet Explorer 9</h1>
  		<p> Windows Internet Explorer 9(缩写为 IE9 )在2011年3月14日21:00 发布。</p>
	</article>
</body>
```

### 12.4 HTML5\<nav>元素
\<nav>标签定义导航链接的部分

### 12.5 HTML5\<aside>元素
\<aside>标签定义页面主区域内容外的内容，如侧边栏。

### 12.6 HTML5\<header>元素
\<header>元素描述了文档的头部区域，在页面中可以使用多个\<header>元素

### 12.7 HTML5\<footer>元素
\<footer>元素描述了文档底部区域，一个页脚通常包含文档的作者、联系信息等
##### 代码：
```html
<footer>
 	<p>Posted by: Hege Refsnes</p>
  	<p><time pubdate datetime="2012-03-01"></time></p>
</footer>
```

### 12.8 HTML5\<figure>和\<figcaption>元素
\<figure>标签规定独立的流内容，如图像、图表和代码等。\<figcaption>标签定义\<figure>元素的标题。
##### 代码:
```html
<figure>
	<img src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" width="304px" height="228px">
	<figcaption>thinking_fioa的头像</figcaption>
</figure>
```

## 13 HTML5 Web存储
HTML5web存储，一个比cookie更好的本地存储方式，可以在本次存储用户的浏览数据。客户端存储数据的两个对象为:

- 1.localStorage:没有时间限制的数据存储
- 2.sessionStorage:针对一个session的数据存储

## 14 HTML5 Web Workers
当HTML页面执行脚本时，页面的状态是不可相应，直到脚本完成。web worker是运行在后台JavaScript，独立于其他脚本，不影响页面的性能。
### 14.1 案例代码(实现计数器): - 未跑通
```html
<body>
	<div>
		<span>计数:</span>
		<output id="rusult">0</output>
	</div>
	<button id="startButton" onclick="startWorker()">开始工作</button>
	<button id="endButton" onclick="endWorker()">停止工作</button>

	<script>
		var w;
		function startWorker() {
			if(typeof(Worker) !== "undefined") {
				if(typeof(w) == "undefined"){
					w = new Worker("demo_workers.js"); // 执行一段Js脚本
				}
				w.onmessage = function(event) {
					document.getElementById("result").innerHTML=event.data;
				}
			} else {
				document.getElementById("result").innerHTML = "抱歉，你的浏览器不支持 Web Workers...";
			}
			
		}
		function endWorker() {
			w.terminate();
			w = undefined;
		}
	</script>
</body>
```

### 14.2 Web Workers和DOM
由于web worker位于外部文件中，因此无法访问下列JavaScript对象:

- 1.window对象
- 2.document对象
- 3.parent对象




