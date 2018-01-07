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































