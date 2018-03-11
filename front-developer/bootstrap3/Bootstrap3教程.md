# 一、Bootstrap3教程
```
@author 鲁伟林
Bootstrap3是目前最受欢迎的前端框架，非常重要。
参考网址是：http://www.runoob.com/bootstrap/bootstrap-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/bootstrap3/
```
---



## 1. Bootstrap简介
Bootstrap是一个快速开发Web应用程序和网站的前端框架。Bootstrap的学习需要先初步了解Html、Css、Javascript基础知识。

### 1.1 Bootstrap 包含的内容
- 1.基本结构：Bootstrap提供了一个带有网格系统、链接样式、背景的基本结构
- 2.CSS：Bootstrap提供多种基本的CSS的常用组件
- 3.组件：Bootstrap包含了十几个可重用的组件
- 4.JavaScript插件：Bootstrap包含了十几个自定义的jQuery插件

## 2. Bootstrap环境安装
Bootstrap安装有两种方法:

- 1.下载Bootstrap，具体地址：[地址](http://getbootstrap.com/) 
- 2.使用CDN服务。国内推荐使用：[https://www.staticfile.org/](https://www.staticfile.org/) ;国外推荐使用：[https://cdnjs.com/](https://cdnjs.com/)

### 2.1 文件结构
如果下载的是Bootstrap已经编译的版本，解压ZIP文件，将看到下面的文件/目录结构:

![](http://www.runoob.com/wp-content/uploads/2014/06/compiledfilestructure.jpg)

如果下载了Bootstrap源代码,那么文件结构如下:

![](http://www.runoob.com/wp-content/uploads/2014/06/sourcecodefilestructure.jpg)

### 2.2 HTML中使用Bootstrap模版
需要包含jquery.js、bootstrap.min.js、bootstrap.min.css文件，用于让常规的HTML变为使用Bootstrap模版

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>Bootstrap模版</title>
    <link href="./bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="./bootstrap/js/bootstrap.min.js"></script>
    <script src="./jquery/jquery-3.2.1.min.js"></script>
</head>
```

# 二、 Bootstrap CSS

## 3. Bootstrap CSS概览
本章将学习Bootstrap底层结构的关键部分和一些最佳实践

### 3.1 HTML5文档类型(Doctype)
Bootstrap中使用了HTML5元素和CSS属性，所以必须使用HTML5文档类型(Doctype)，通常的Bootstrap项目请用以下代码开头
##### 代码:
```html
<!DOCTYPE html>
<html>
.....
</html>
```

### 3.2 移动设备优先
- 1.Bootstrap3的设计目标是移动设备优先，然后才是桌面设备
- 2.Bootstrap3开发的网站兼容移动设备，确保适当的绘制和触屏缩放
- 3.width=device-width属性控制设备宽度，即使不同的设备带有不同的屏幕分辨率，也能保证完美的呈现
- 4.initial-scale=1.0确保页面加载时，以1:1的比例呈现，不会有任何缩放
- 5.user-scalable=no禁用其缩放功能
- 6.maximum-scale=1.0与user-scalable=no同时使用时，用户可以滑动屏幕

##### 代码:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```

## 4. Bootstrap 网格系统
Bootstrap提供一套响应式、移动设备优先的流式网格系统，随着不同设备屏幕或视口(viewport)尺寸的增加，系统会自动分为最多12列，以自动适配屏幕变化

[](https://github.com/thinkingfioa/Notes/blob/master/uploadPics/Bootstrap3-4.png)

### 4.1 Bootstrap网格系统(Grid System)工作原理
网格系统通过一系列包含内容的行和列来创建页面布局。下面列出了Bootstrap网格系统如果工作的:

- 1.行必须放置在.container class内，以便获得适当的对齐(alignment)和内边距(padding)
- 2.使用行来创建列的水平组
- 3.内容应该放置在列内，且唯有列可以是行的直接子元素
- 4.预定义的网格类，比如.row和.col-xs-4，可用于快速创建网格布局。LESS混合类可用于更多的语义布局
- 5.列通过内边距(padding)来创建内容间的间隙
- 6.网格系统是通过指定想要横跨的十二个可用的列来创建的。例如：要创建三个相等的列，则使用三个.col-xs-4

## 5. Bootstrap 排版
使用Bootstrap的排版特性，可以创建标题、段落、列表及其他内联元素

### 5.1 标题(h1-h6)
Bootstrap定义了所有的HTML标题(h1到h6)的样式。提醒：使用Bootstrap模版时，需要使用3个文件:bootstrap.min.css、bootstrap.min.js、jquery.min.js。**后面的代码样例将省略\<head\>头**
##### 代码：
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Bootstrap</title>
    <link href="./bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <script src="./bootstrap/js/bootstrap.min.js"></script>
    <script src="./jquery/jquery-3.2.1.min.js"></script>
</head>
<body>
    <h1>我是标题1 h1</h1>
    <h2>我是标题2 h2</h2>
    <h3>我是标题3 h3</h3>
    <h4>我是标题4 h4</h4>
    <h5>我是标题5 h5</h5>
    <h6>我是标题6 h6</h6>
</body>
</html>
```

### 5.2 内联子标题(small)
如果需要向任何标题添加一个内联子标题，需要在元素两旁添加<smalll>或者添加.small class。将得到一个字号更小、颜色更浅的文本。
##### 代码:
```html
<body>
    <h1>我是标题1 h1 <small>副标题h1.1</small></h1>
    <h2>我是标题2 h2</h2>
    <h3>我是标题3 h3 <small>副标题h3.1</small></h3>
    <h4>我是标题4 h4</h4>
</body>
```

### 5.3 引导主体副本(lead)
使用class="lead"来给段落添加强调文本，得到更大更粗、更高的文本。
##### 代码:
```html
<body>
    <h2>引导主体副本</h2>
    <p class="lead">
        这是一个演示引导主体副本用法的实例。
        这是一个演示引导主体副本用法的实例。
    </p>
</body>
```

### 5.4 强调
Bootstrap提供了一些用于强调文本的类

- 1.small: 文本为父文本大小的85%
- 2.strong: 设置文本变粗体
- 3.em: 文本斜体
- 4.class="text-left": 向左对齐
- 5.class="text-center": 居中对齐
- 6.class="text-right": 向右对齐
- 7.class="text-muted": 文本内容减弱
- 8.class="text-primary": primary class效果
- 9.class="text-success": success class效果
- 10.class="text-info": info class效果
- 11.class="text-warning": warning class效果 
- 12.class="text-danger": danger class效果

##### 代码:
```html

<body>
    <small>本行内容-small</small><br>
    <strong>本行内容-strong</strong><br>
    <em>本行内容-em</em><br>
    <p class="text-left">本行内容-left</p>
    <p class="text-center">本行内容-center</p>
    <p class="text-right">本行内容-right</p>
    <p class="text-muted">本行内容-muted</p>
    <p class="text-primary">本行内容-primary</p>
    <p class="text-success">本行内容-success</p>
    <p class="text-info">本行内容-info</p>
    <p class="text-warning">本行内容-warning</p>
    <p class="text-danger">本行内容-danger</p>
</body>
```

### 5.5 缩写（abbr)
- 1.Bootstrap利用\<abbr>元素样式，定义缩写效果：底部有一条虚线边框+鼠标悬停提示完整文本
- 2.利用class=".initialism"来得到更小字体的文本

##### 代码:
```html
<body>
    <abbr title="World Wide Web">WWW</abbr><br/>
    <abbr title="thinking_fioa" class=".initialism">TF</abbr>
</body>
```

### 5.6 地址(Address)
使用\<address\>标签，可以用来在网页上显示联系信息。

##### 代码:
```html
<body>
    <address>
        <strong>Some Company, Inc.</strong>
        007 street<br>
        Some City, State XXXXX<br>
        <abbr title="Phone">P:</abbr>1373814XXXX<br>
    </address>
    <address>
        <Strong>Email: </Strong>
        <a href="mailto:#">thiking_fioa@163.com</a>
    </address>
</body>
```

### 5.7 引用(Blockquote)
- 1.使用默认的\<blockquote\>来显示引用
- 2.默认的\<blockquote\>是左对齐
- 3.class="pull-right"是定义右对齐

##### 代码:
```html
<body>
    <blockquote>
        一个带有源标题的引用
        <small>Someone famous in <cite title="Source Title">Source Title</cite></small>
    </blockquote>
    <blockquote class="pull-right">
        一个向右对齐的标题引用
        <small>Someone famous in <cite title="Source Title">Source Title</cite></small>
    </blockquote>
</body>
```

### 5.8 列表
Bootstrap 支持有序列表、无序列表和定义列表

- 1.class="list-unstyled": 未定义样式列表
- 2.class="list-inline":将所有列表项放置同一行

##### 代码:
```html
<body>
	<h4>有序列表</h4>
	<ol>
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ol>
	<h4>无序列表</h4>
	<ul>
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ul>
	<h4>未定义样式列表</h4>
	<ul class="list-unstyled">
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ul>
	<h4>内联列表</h4>
		<ul class="list-inline">
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ul>
	<h4>定义列表</h4>
	<dl>
		<dt>Description 1</dt>
		<dd>Item 1</dd>
		<dt>Description 2</dt>
		<dd>Item 2</dd>
	</dl>
	<h4>水平的定义列表</h4>
	<dl class="dl-horizontal">
		<dt>Description 1</dt>
		<dd>Item 1</dd>
		<dt>Description 2</dt>
		<dd>Item 2</dd>
	</dl>
</body>
```
















