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




























