# 一、Bootstrap3基础教程
```
@author 鲁伟林
Bootstrap3是目前最受欢迎的前端框架，非常重要。本教材不包括: Bootstrap插件，有关插件知识，请看另一篇博客
参考网址是：http://www.runoob.com/bootstrap/bootstrap-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/bootstrap3/
```
---

## 特别说明
Bootstrap3中一个标签往往同时有col-xs、col-sm、col-md、col-lg。如何理解，看下解释:

- 1.col-xs- 超小屏幕 手机(<768px)
- 2.col-sm- 小屏幕 平板(>=768px)
- 3.col-md- 中等屏幕 桌面显示器(>=992px)
- 4.col-lg- 大屏幕 大桌面显示器(>=1200px)

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
    <script src="./jquery/jquery-3.2.1.min.js"></script>
    <script src="./bootstrap/js/bootstrap.min.js"></script>
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

##### 特别说明:
Bootstrap3中一个标签往往同时有col-xs、col-sm、col-md、col-lg。如何理解，看下解释:

- 1.col-xs- 超小屏幕 手机(<768px)
- 2.col-sm- 小屏幕 平板(>=768px)
- 3.col-md- 中等屏幕 桌面显示器(>=992px)
- 4.col-lg- 大屏幕 大桌面显示器(>=1200px)

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
    <script src="./jquery/jquery-3.2.1.min.js"></script>
    <script src="./bootstrap/js/bootstrap.min.js"></script>
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

## 6. Bootstrap 代码
Bootstrap允许使用两种方式显示代码:

- 1.第一种是\<code\>标签。如果想要内联显示代码，就应该使用\<code\>标签
- 2.第二种是\<pre\>标签。如果想要用独立的块元素显示代码，则使用\<pre\>标签
- 3.开始和结束标签，请使用unicode变体: \&lt(\<);和\&gt(\>)

##### 代码:
```html
<body>
    <p><code>&lt;header&gt;</code>作为内联元素被包围</p>
    <div>
        <span>如果需要将代码作为一个独立的块元素，需要使用标签:pre</span>
    </div>
    <pre>
        &lt;article&gt;
            &lt;h1&gt;Article Heading&lt;/h1&gt;
        &lt;/article&gt;
    </pre>
</body>
```

## 7. Bootstrap 表格
Bootstrap提供了一个清晰的创建表格的布局。Bootstrap支持的一些表格元素如下表:

|标签|描述|
|:---:|:---:|
|\<table\>|为表格添加基础样式|
|\<thead\>|表格标题行的容器元素，用来标识表格列|
|\<tbody\>|表格主体中的表格行的容器元素|
|\<tr\>|一组出现在单行上的表格单元格的容器元素|
|\<td\>| 默认的表格单元格|
|\<th\>|特殊的表格单元格，用来标识列或行。必须在\<thea\>内使用|
|\<caption\>|	关于表格存储内容的描述或总结|

### 7.1 表格类
下列样式可用于表格:

- 1.(.table): 为任意\<table\>添加基本样式(只有横向分割线)
- 2.(.table-striped): 为\<tbody\>内添加斑马线形式条纹
- 3.(.table-bordered): 为所有表格的单元格添加边框
- 4.(.table-hover): 在\<tbody\>内的任一行启用鼠标悬停状态
- 5.(.table-condensed): 让表格更加紧凑

##### 代码:
```html
<table class="table table-striped table-bordered table-hover table-condensed">
	<caption>姓名表格</caption>
    <thead>
        <tr>
            <th>#</th>
            <th>Firstname</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>luweilin</td>
        </tr>
        <tr>
            <td>2</td>
            <td>thinking_fioa</td>
        </tr>
        <tr>
            <td>3</td>
            <td>pppp</td>
        </tr>
    </tbody>
</table>
```

### 7.2 \<tr\>、\<th\>、\<td\>类
下列类可用于表格的行或单元格

- 1.(.active): 将悬停的颜色应用于行或单元格
- 2.(.success): 表示成功的操作
- 3.(.info): 表示信息变化的操作
- 4.(.warning): 表示一个警告的操作
- 5.(.danger): 表示一个危险的操作

##### 代码:
```html
<body>
    <div class="container">
        <h1>表格</h1>
        <div>
            所有属性都用上来:
        </div>
        <table class="table">
            <caption>编号表格:</caption>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Firstname</th>
                </tr>
            </thead>
            <tbody>
                <tr class="active">
                    <td>1</td>
                    <td>luweilin-active</td>
                </tr>
                <tr class="success">
                    <td>2</td>
                    <td>thinking_fioa-success</td>
                </tr>
                <tr class="info">
                    <td>3</td>
                    <td>pppp-info</td>
                </tr>
                <tr class="warning">
                    <td>4</td>
                    <td>tzj-warning</td>
                </tr>
                <tr class="danger">
                    <td>5</td>
                    <td>lbf-danger</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
```

### 7.3 响应式表格
通过将任意的.table包在.table-responsive内，可以让表格滚动，以适应小型设备和大型设备
###### 代码:
```html
<body>
	<div class="table-responsive">
		<table class="table">
			<caption>表格</caption>
			<thead>
			</thead>
			<tbody>
			</tbody>
		</table>
	</div>
</body>
```

## 8. Bootstrap表单
Bootstrap通过一些简单的HTML标签和扩展的类即可创建出不同样式的表单


### 8.1 表单布局
Bootstrap提供了下列类型的表单布局：

- 1.垂直表单(默认)
- 2.内联表单
- 3.水平表单

### 8.2 垂直或基本表单
基本的表单结构是Bootstrap自带的，下面列出创建一个基本表单的步骤：

- 1.向父\<form\>元素添加role="form"
- 2.把标签和控件放在一个带有class .form-group的\<div\>中。这是获取最佳间距所必需的
- 3.向所有的文本元素\<input\>、\<textarea\>和\<select\>添加class="from-control"

##### 代码:
```html
 <form role="form">
	<div class="form-group">
		<label for="name">名称</label>
		<input type="text" class="form-control" id="name" placeholder="请输入名称">
	</div>
	<div class="form-group">
		<label for="inputfile">文件输入</label>
		<input type="file" id="inputfile">
		<p class="help-block">这里是块级帮助本文的实例</p>
	</div>
	<div class="form-group">
		<label>
			<input type="checkbox"> 请打勾
		</label>
	</div>
	<button type="submit" class="btn btn-default">提交</button>
</form>
```

### 8.3 内联表单
- 1.创建一个表单，希望它的所有元素都是内联的，向左对齐的，标签是并排的。请在\<form\>标签中添加 class .form-inline
- 2.默认情况下，Bootstrap中的input、select和textarea有100%宽度。在使用内联表单时，需要在表单控件上设置一个宽度

##### 代码:
```html
<body>
    <form role="form" class="form-inline">
        <div class="form-group">
            <label class="sr-only" for="name">名称</label>
            <input type="text" class="form-control" id="name" placeholder="请输入名称">
        </div>
        <div class="form-group">
            <label class="sr-only" for="inputfile">文件输入</label>
            <input type="file" id="inputfile">
        </div>
        <div class="form-group">
            <label>
                <input type="checkbox">请打勾
            </label>
        </div>
        <button type="submit" class="btn btn-default">提交</button>
    </form>
</body>
```

### 8.4 水平表单
水平表单与其他表单不仅标记的数量上不同，而且表单的呈现形式也不同。具体按下面几个步骤

- 1.向父\<form\>元素添加class .form-horizontal
- 2.把标签和控件放在一个带有class .form-group的\<div\>中
- 3.向标签添加class .control-label

##### 代码:
```html
<form role="form" class="form-horizontal">
    <div class="form-group">
        <label for="firstname" class="col-sm-2 control-label">名字</label>
        <div class="col-sm-10">
            <input type="text" id="firstname" class="form-control" placeholder="请输入名字">
        </div>
    </div>
    <div class="form-group">
        <lable for="lastname" class="col-sm-2 control-label">姓</lable>
        <div class="col-sm-10">
            <input type="text" id="lastname" class="form-control" placeholder="请输入姓">
        </div>
    </div>
    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
            <div class="checkbox">
                <label>
                    <input type="checkbox">请记住我
                </label>
            </div>
        </div>
    </div>
    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
            <button type="submit" class="btn btn-default">登录</button>
        </div>
    </div>
</form>
```

### 8.5 支持的表单控件
Bootstrap支持最常见的表单控件，主要是：input、textarea、checkbox、radio和select

### 8.6 输入框(input)
Bootstrap提供所有原生的HTML5的input类型的支持，包括:text、password、detetime、detetime-local、date、month、time、week、number、email、url、search、tel和color

- 下面代码中:for="text"表示点击\<label\>标签后，焦点会聚焦到id="text"的输入框

##### 代码：
```html
<form role="form">
	<div class="form-group">
		<label for="test">试试看</label>
		<input type="text" id="test" class="form-control" placeholder="试试看">
	</div>
</form>
```

### 8.7 文本框(Textarea)
文本框(Textarea)提供多行输入。属性rows规定显示行数

##### 代码:
```html
<form role="form">
	<div class="form-group">
		<lable for="name">文本框</lable>
		<textarea class="form-control" rows="3"></textarea>
	</div>
</form>
```

### 8.8 复选框(Checkbox)和单选框(Radio)
 
 - 1.checkbox提供用于从列表中选择若干个选项，而radio限制用户只能选择一个选项
 - 2.使用class .checkbox-inline或.radio-inline，控制它们显示在同一行

##### 代码:
```html
<label for="name">复选框和单选按钮</label>
<div class="checkbox">
    <label><input type="checkbox" value="choose1">选项一</label>
</div>
<div class="checkbox">
    <label><input type="checkbox" value="choose2">选项二</label>
</div>
<div class="radio">
    <label><input type="radio" name="optionsRadios" id="optionsRadios1" vlaue="radio1" checked>选项1</label>
</div>
<div class="radio">
    <label><input type="radio" name="optionsRadios" id="optionsRadios2" value="radio2">选项2</label>
</div>

<label for="name">内联的复选框和单选框</label><br>
<div class="checkbox-inline">
    <label><input type="checkbox" id="inlineCheckbox1" value="option1">选项1</label>
</div>
<div class="checkbox-inline">
    <label><input type="checkbox" id="inlineCheckbox2" value="option2">选项2</label>
</div>
<div class="checkbox-inline">
    <label><input type="checkbox" id="inlineCheckbox3" value="option3">选项3</>
</div>
<div class="radio-inline">
    <label><input type="radio" name="optionsRadiosinline" id="optionsRadio3" value="option1" checked>选项一</label>
</div>
<div class="radio-inline">
    <label><input type="radio" name="optionsRadiosinline" id="optionsRadio4" value="option2">选项二</label>
</div>
```

### 8.9 选择框(Select)
选择框允许用户从多个选项中进行选择，默认情况下只能选择一个选项

- 1.使用\<select\>展示列表选项，通常是用户熟悉的选择列表
- 2.使用multiple="multiple"允许用户选择多个选项

##### 代码：
```html
<form role="form">
    <div class="form-group">
        <label for="name">选择列表</label>
        <select class="form-control">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
    </div>
    <div class="form-group">
        <label for="name">可多选的选择列表</label>
        <select multiple class="form-control">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
        </select>
    </div>
</form>
```

### 8.10 静态控件
当需要在一个水平表单内的表单标签后放置纯文本时，需要在\<p\>上使用class .form-control-static

##### 代码:
```html
<form role="form" class="form-horizontal">
    <div class="form-group">
        <label for="emailAddress" class="col-sm-2 control-label">Email</label>
        <p class="form-control-static" id="emailAddress">thinking_fioa@163.com</p>
    </div>
    <div class="form-group">
        <label for="inputPassword" class="col-sm-2 control-label">密码</label>
        <div class="col-sm-10">
            <input type="password" id="inputPassword" class="c" name="pwd" placeholder="请输入密码">
        </div>
    </div>
</form>
```

### 8.11 表单控件状态

- 1.输入框焦点：当输入框(input)接收到focus时，输入框的轮廓会被移除，同时应用box-shadow
- 2.禁用的输入框input：使用属性disabled禁用输入框
- 3.禁用的字段集fieldset：对\<fieldset\>添加disabled属性来禁用\<fieldset\>内的所有控件
- 4.验证状态：对父元素简单的添加适当的class(.has-warning、has-error或.has-success)即可验证

##### 代码:
```html
<form role="form" class="form-horizontal">
    <div class="form-group">
        <label class="col-sm-2 control-label">聚焦</label>
        <div class="col-sm-10">
            <input type="text" class="form-control" placeholder="请输入框获得焦点...">
        </div>
    </div>
    <div class="form-group">
        <label class="col-sm-2 control-label">禁用</label>
        <div class="col-sm-10">
            <input type="text" class="form-control" placeholder="该输入框禁止输入..." disabled>
        </div>
    </div>
    <fieldset disabled>
        <div class="form-group">
            <label class="col-sm-2 control-label">禁止选择菜单</label>
            <div class="col-sm-10">
                <select class="form-control">
                    <option>禁止选择</option>
                </select>
            </div>
        </div>
    </fieldset>
    <div class="form-group has-error">
        <label class="col-sm-2 control-label" for="inputWarning">输入告警</label>
        <div class="col-sm-10">
            <input type="text" class="form-control" id="inputWarning">
        </div>
    </div>
</form>
```

### 8.12 表单控件大小
使用class .input-lg和.col-lg-* 来设置表单的高度和宽度

- 1.input-lg: 放大表单高度
- 2.input-sm: 缩小表单高度
- 3.col-lg-*: 表示在大屏幕上占用几个格子。如: col-sm-10表示在小屏幕该div占用10个列的宽度

### 8.13 表单帮助文本(help-block)
表单控件可以在输入框input上有一个块级帮助文本，使用.help-block来占用整个宽度的内容块

##### 代码：
```html
<form role="form">
    <span>帮助文本实例</span>
    <input class="form-control" type="text" placeholder="">
    <span class="help-block">说明文档</span>
</form>
```

## 9. Bootstrap 按钮
任何带有class .btn的元素都会继承圆角灰色按钮。下列样式同样适用于\<a\>、\<button\>和\<input\>

- 1.btn：为按钮添加基本样式
- 2.btn-default：默认／标准按钮
- 3.btn-success(primary/info/warning/danger)：表示成功等的动作
- 4.btn-link：让按钮看起来像链接(仍然保留按钮行为)
- 5.btn-lg(btn-sm/xs)：制作一个大按钮等
- 6.btn-block：块级按钮
- 7.active：按钮被点击
- 8.disabled：禁用按钮

##### 代码:
```html
<button type="button" class="btn btn-info">警告按钮</button>
```

### 9.1 按钮状态
Bootstrap提供了激活、禁用等按钮状态的class

- 1.激活状态(active)：激活状态呈现被压的外观(深色的背景、深色的边框、阴影)
- 2.禁用状态(disabled)：禁用一个按钮时，它的颜色会变淡50%，并失去渐变

##### 代码:
```html
<p>
    <button type="button" class="btn btn-default">默认按钮</button>
</p>
<p>
    <button type="button" class="btn btn-default active">激活按钮</button>
</p>
<p>
    <button type="button" class="btn btn-default disabled">禁用按钮</button>
</p>
```

## 10. Bootstrap 图片
Bootstrap提供了三个对图片应用的简单样式的class：

- 1.img-rounded：将图片变成圆角，通过添加border-radius:6px来实现
- 2.img-circle：将图片变成圆形，通过添加border-radius：50%来实现
- 3.img-thumbnail：添加内边框效果，通过内边距(padding)和一个灰色的边框来实现
- 4.img-responsive：让图片支持响应式设计。图片可以很好的扩展到父元素。使用max-width:100%和height:auto来实现

## 11. Bootstrap 辅助类
Bootstrap定义了诸多辅助类

### 11.1 文本
不同的类展示不同的文本颜色。包括链接标签\<a\>文本也起同样的效果

- 1.text-muted：文字变弱的样式
- 2.text-primary
- 3.text-success
- 4.text-info
- 5.text-warning
- 6.text-danger

##### 代码：
```html
<div class="container">
    <p class="text-danger">使用text-danger样式文本</p>
    <a class="text-danger" href="http://write.blog.csdn.net/postlist">链接文本使用text-danger</a>
</div>
```

### 11.2 背景
不同的类展示不同的背景颜色。如果是链接，鼠标移上去文本会变暗

- 1.bg-primary
- 2.bg-success
- 3.bg-info
- 4.bg-warning
- 5.bg-danger

##### 代码:
```html
<div class="container">
    <p class="bg-danger">使用bg-danger样式文本</p>
    <a class="bg-danger" href="http://write.blog.csdn.net/postlist">链接文本使用bg-danger</a>
</div>
```

### 11.3 其他

- 1.pull-left：元素浮动在左边
- 2.pull-right：元素浮动在右边
- 3.center-block：设置元素为display:block并居中显示
- 4.clearfix：清除浮动
- 5.show：强制元素显示
- 6.hidden：强制元素隐藏
- 7.sr-only：除了屏幕阅读器外，其他设备上隐藏元素
- 8.sr-only-focusable：与 .sr-only 类结合使用，在元素获取焦点时显示(如：键盘操作的用户)
- 9.text-hide：将页面元素所包含的文本内容替换为背景图
- 10.close：显示关闭按钮	
- 11.caret：显示下拉式功能

### 11.4 关闭标签
使用class close得到关闭标签。

##### 代码:
```html
<button type="button" class="close" aria-hidden="true">&times;</button>
```

# 二、Bootstrap 布局组件

## 12. Bootstrap 字体图标(Glyphicons)
字体图标是在Web项目中使用的图标字体。可以在fonts文件夹内找到字体图标。字体图标列表：[字体图标](http://www.runoob.com/try/demo_source/bootstrap3-glyph-icons.htm)

### 12.1 用法
如需要使用图标，只需使用下列代码即可。

##### 代码:
```html
<span class="glyphicon glyphicon-user"></span>
```

### 12.2 带有字体图标的导航栏
##### 代码:
```html
<div class="navbar navbar-fixed-top navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Project name</a>
        </div>
        <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#"><span class="glyphicon glyphicon-home"></span>Home</a></li>
                <li><a href="#shop"><span class="glyphicon glyphicon-shopping-cart"></span>Shop</a></li>
                <li><a href="#support"><span class="glyphicon glyphicon-headphones"></span>Support</a></li>
            </ul>
        </div>
    </div>
</div>
```

### 12.3 定制字体图标和尺寸
##### 代码:
```html
<button type="button" class="btn btn-primary btn-lg">
    <span class="glyphicon glyphicon-user"></span>User
</button>
```

## 13. Bootstrap 下拉菜单(Dropdowns)
Bootstrap下拉菜单是可切换的，是以列表格式显示链接的上下文菜单

##### 代码:
```html
<div class="dropdown">
    <button type="button" class="btn dropdown-toggle" id="dropdownMenu1" data-toggle="dropdown">
        主题
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">Java</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">数据挖掘</a>
        </li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">编译原理</a>
        </li>
        <li role="presentation" class="divider"></li>
        <li role="presentation">
            <a role="menuitem" tabindex="-1" href="#">计算机操作系统</a>
        </li>
    </ul>
</div>
```

### 13.1 选项

- 1.pull-right(对齐)：通过向dropdown-menu中添加class .pull-right来向右对齐下拉菜单
- 2.dropdown-header(标题)：使用dropdown-header向下拉菜单的标签区域添加标题
- 3.dropup：指定向上弹出的下拉菜单
- 4.disabled：下拉菜单中的禁用项
- 5.divider：下拉菜单中的分割线

## 14. Bootstrap 按钮组
按钮组允许多个按钮被折叠在同一行

- 1.btn-group：用于形成基本的按钮组，在btn-group中放置一系列带有class .btn按钮
- 2.btn-tooler：用于将几组\<div class="btn-group"\>结合在一起
- 3.btn-group-lg(btn-group-sm,btn-group-xs)：整个按钮组的大小控制
- 4.btn-group-vertical：让一组按钮垂直堆叠显示

### 14.1 基本按钮组(btn-group)
btn-group用于形成按钮组，位于同一行中。

##### 代码：
```html
<div class="btn-group">
    <button type="button" class="btn btn-default">按钮1</button>
    <button type="button" class="btn btn-danger">按钮2</button>
    <button type="button" class="btn btn-info">按钮3</button>
</div>
```

### 14.2 按钮工具栏(btn-toolbar)
btn-toolbar用于将几个按钮组合并在一起

##### 代码:
```html
<div class="btn-toolbar" role="toolbar">
	<div class="btn-group">
		<button type="button" class="btn btn-default">按钮1</button>
		<button type="button" class="btn btn-default">按钮2</button>
	</div>
	<div class="btn-group">
		<button type="button" class="btn btn-default">按钮3</button>
		<button type="button" class="btn btn-default">按钮4</button>
	</div>
</div>
```

### 14.3 按钮的大小(btn-gruop-sm)
btn-group-sm用于控制按钮大小，如：\<div class="btn-group btn-group-sm"\>

### 14.4 嵌套
可以在一个按钮组内嵌套另一个按钮组，如果下拉菜单和一系列的按钮组使用时，则用到

##### 代码:
```html
<div class="btn-group">
    <button type="button" class="btn btn-default">按钮1</button>
    <button type="button" class="btn btn-default">按钮2</button>
    <div class="btn-group">
        <button type="button" class="btn btn-info dropdown-toggle" data-toggle="dropdown">
            <span>下拉</span>
            <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" role="menu">
            <li><a href="#">下拉链接 1</a></li>
            <li><a href="#">下拉链接 2</a></li>
        </ul>
    </div>
</div>
```

### 14.5 垂直的按钮组(btn-group-vertical)
使用btn-group-vertical来让按钮垂直显示

## 15. Bootstrap 按钮下拉菜单
Bootstrap支持向按钮添加下拉菜单，具体代码可参考14.4中的

### 15.1 分割的按钮下拉菜单(divider)
使用class .divider来实现分割下拉。代码: \<li class="divider"\>\</li\>

### 15.2 按钮下拉菜单的大小(btn-lg)
使用class .btn-lg、btn-sm和btn-xs来指定按钮大小

##### 代码：
```html
<div class="btn-group">
    <button type="button" class="btn btn-default btn-lg dropdown-toggle" data-toggle="dropdown">
        <span>默认下拉菜单</span>
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li><a href="#">功能1</a></li>
        <li><a href="#">功能2</a></li>
        <li class="divider"></li>
        <li><a href="#">分割线后的功能1</a></li>
    </ul>
</div>
```

### 15.3 按钮上拉菜单(dropup)
菜单也可以往上拉，只需要在class .btn-group中添加class .dropup

## 16. Bootstrap 输入框组(form-control)
使用输入框组，可以很容易向基于文本的输入框添加作为前缀和后缀的文本或按钮。向form-control添加前缀或后缀元素的基本步骤如下:

- 1.把前缀或后缀元素放在一个带有class .input-group中的\<div\>中
- 2.添加class .input-group-addon的\<span\>中添加前缀内容
- 3.补充input元素输入框

##### 代码：
```html
<div class="input-group">
	<span class="input-group-addon">前缀内容</span>
	<input type="text" class="form-control" placeholder="缺省提示内容">
</div>
```

### 16.1 输入框组的大小
添加表单大小(input-group-lg、input-group-sm)来改变输入框组的大小

##### 代码：
```html
 <div style="padding: 100px 100px 10px;" >
        <form class="bs-example bs-example-form" role="form">
            <div class="input-group input-group-lg">
                <span class="input-group-addon">@</span>
                <input type="text" class="form-control" placeholder="请输入邮箱">
            </div>
        </form>
    </div>
```

### 16.2 复选框和单选框插件
可以将复选框和单选框作为输入框的前缀或后缀元素

##### 代码:
```html
<div style="padding: 100px 100px 10px;">
    <form class="bs-example bs-example-form" role="form">
        <div class="row">
            <div class="col-lg-6">
                <div class="input-group">
                    <span class="input-group-addon"><input type="checkbox"></span>
                    <input type="text" class="form-control">
                </div>
            </div>
            <div class="col-lg-6">
                <div class="input-group">
                    <span class="input-group-addon"><input type="radio"></span>
                    <input type="text" class="form-control">
                </div>
            </div>
        </div>
    </form>
</div>
```

### 16.3 按钮插件
可以将按钮作为输入框组的前缀或后缀元素。此时，不需要使用class .input-group-addon，而使用class .input-group-btn来包裹按钮

##### 代码:
```html
<div style="padding: 100px 100px 10px;">
    <form class="bs-example bs-example-from" role="form">
        <div class="row">
            <div class="col-lg-6">
                <div class="input-group">
                    <span class="input-group-btn">
                        <button class="btn btn-default">Go!</button>
                    </span>
                    <input type="text" class="form-control">
                </div>
            </div>
            <div class="col-lg-6">
                <div class="input-group">
                    <span class="input-group-btn">
                        <button class="btn btn-info">Stop!</button>
                    </span>
                    <input type="text" class="form-control">
                </div>
            </div>
        </div>
    </form>
</div>
```

## 17. Bootstrap 导航元素
Bootstrap提供用于定义导航元素的一些选项。使用相同的标记和基类.nav

### 17.1 表格导航或标签(nav-tabs)
创建一个标签式的导航菜单：

- 1.以一个带有class .nav的无序列表开始
- 2.添加class .nav-tabs

##### 代码:
```html
<ul class="nav nav-tabs">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">iMac</a></li>
    <li><a href="#">iPhone</a></li>
    <li><a href="#">Mac</a></li>
</ul>
```

### 17.2 胶囊式的导航菜单(nav-pills)
如果需要将标签改成胶囊式，只需要将class .nav-pills替换class .nav-tabs即可

##### 代码:
```html
<ul class="nav nav-pills">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">iMac</a></li>
    <li><a href="#">iPhone></a></li>
    <li><a href="#">Mac</a></li>
</ul>
```

### 17.3 垂直的胶囊式导航菜单(nav-stacked)
在使用calss .nav和class .nav-pills的同时使用class .nav-stacked，让胶囊垂直堆叠

##### 代码:
```html
<ul class="nav nav-pills nav-stacked">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">iPad</a></li>
    <li><a href="#">iMac</a></li>
    <li><a href="#">iPhone</a></li>
</ul>
```

### 17.4 两端对齐的导航(nav-justified)
当屏幕宽度大于768px时，在使用表格式导航(nav nav-tabs)和胶囊式导航(nav nav-pills)时，请同时使用class .nav-justified。以让导航的长度和父元素等宽。

### 17.5 禁用链接(disabled)
对每个class .nav添加class .disabled，则会创建一个灰色的链接

##### 代码:
```html
<ul class="nav nav-tabs nav-justified">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">iPad</a></li>
    <li><a href="#">iPhone</a></li>
    <li class="disabled"><a href="#">iMac(禁用链接)</a></li>
    <li><a href="#">iWatch</a></li>
</ul>
```

### 17.6 带有下拉菜单的标签
向一个标签添加下拉菜单的步骤如下:

- 1.以一个带有class .nav的无序列表开始
- 2.添加class nav-tabs
- 3.添加带有.dropdown-menu的无序列表

##### 代码：
```html
<ul class="nav nav-tabs nav-justified">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">iMac</a></li>
    <li><a href="#">iPad</a></li>
    <li class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
            <span>iPhone</span>
            <span class="caret"></span>
        </a>
        <ul class="dropdown-menu" role="menu">
            <li><a href="#">iPhone-5</a></li>
            <li><a href="#">iPhone-6</a></li>
            <li><a href="#">iPhone-6s</a></li>
            <li class="divider"></li>
            <li><a href="#">iPhone-X</a></li>
        </ul>
    </li>
    <li><a href="#">iWatch</a></li>
</ul>
```

### 17.7 动态标签
与tab-pane和data-toggle="tab"(或data-toggle="pill")一同使用，设置标签页对应的内容随标签切换而更改

##### 代码：
```html
<ul class="nav nav-tabs nav-justified">
    <li class="active"><a data-toggle="tab" href="#home" >Home</a></li>
    <li><a data-toggle="tab" href="#iMac">iMac</a></li>
    <li><a data-toggle="tab" href="#iPhone">iPhone</a></li>
    <li><a data-toggle="tab" href="#iWatch">iWatch</a></li>
</ul>
<div class="tab-content">
    <div id="home" class="tab-pane fade in active">
        <span>首页，欢迎你</span>
    </div>
    <div id="iMac" class="tab-pane fade">
        <span>iMac页面</span>
    </div>
    <div id="iPhone" class="tab-pane fade">
        <span>iPhone页面</span>
    </div>
    <div id="iWatch" class="tab-pane fade">
        <span>iWatch页面</span>
    </div>
</div>
```

## 18. Bootstrap 导航栏
Bootstrap导航栏包含了站点名称和基本导航定义样式

### 18.1 默认的导航栏
创建一个默认导航栏的基本步骤:

- 1.向\<nav\>标签添加class .navbar和class .navbar-default
- 2.向上面的元素添加role="navigation"，有助于增加可访问性
- 3.向\<div\>元素添加一个标题class .navbar-header，内部包含了带有class .navbar-brand的元素\<a\>
- 4.向导航栏添加链接，添加class .nav和class .navbar-nav的无序列表

##### 代码:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">Apple公司</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">iMac</a></li>
            <li><a href="#">iPad</a></li>
            <li class="dropdown">
                <a data-toggle="dropdown" href="#" class="dropdown-toggle">
                    <span>iPhone</span>
                    <span class="caret"></span>
                </a>
                <ul class="dropdown-menu" role="menu">
                    <li><a href="#">iPhone-5s</a></li>
                    <li><a href="#">iPhone-6s</a></li>
                    <li><a href="#">iPhone-7</a></li>
                    <li><a href="#">iPhone-X</a></li>
                </ul>
            </li>
            <li><a href="#">iWatch</a></li>
        </ul>
    </div>
</nav>
```

### 18.2 响应式的导航栏
响应式的导航栏是指点击某按钮后，展开菜单。

##### 代码:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse"
                    data-target="#example-navbar">
                <span class="sr-only">切换导航</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a href="#" class="navbar-brand">Apple公司</a>
        </div>
        <div class="collapse navbar-collapse" id="example-navbar">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">iMac</a></li>
                <li><a href="#">iPad</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        <span>iPhone</span>
                        <span class="caret"></span>
                    </a>
                    <ul class="dropdown-menu" role="menu">
                        <li><a href="#">iPhone-5</a></li>
                        <li><a href="#">iPhone-6s</a></li>
                        <li><a href="#">iPhone-7</a></li>
                        <li><a href="#">iPhone-8</a></li>
                        <li class="divider"></li>
                        <li><a href="#">iPhone-X</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

### 18.3 导航栏中的表单(navbar-form)
导航栏中的表单使用class .navbar-form，其确保了表单适当的垂直对齐和在较窄的窗口中折叠行为。

##### 代码:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Apple公司</a>
        </div>
        <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
                <input type="text" class="form-control" placeholder="输入手机型号">
            </div>
            <button type="submit" class="btn btn-default">提交</button>
        </form>
    </div>
</nav>
```

### 18.4 导航栏中的按钮(navbar-btn)
可以使用class .navbar-btn向不在\<form\>元素中添加\<button\>按钮

##### 代码:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Apple公司</a>
        </div>
        <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
                <input type="text" class="form-control" placeholder="输入手机型号">
            </div>
            <button type="submit" class="btn btn-default">提交</button>
        </form>
        <button type="button" class="btn btn-default navbar-btn">表单外的Button</button>
    </div>
</nav>
```

### 18.5 导航栏中的文本(navbar-text)
使用class .navbar-text向导航栏中添加文本字符串。通常与\<p\>标签一起使用，确保适当的前导和颜色

##### 代码:
```html
<nav role="navigation" class="navbar navbar-default">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Apple公司</a>
        </div>
        <div class="navbar-text">
            <p>我是thinking_fioa.</p>
        </div>
    </div>
</nav>
```

### 18.6 结合图标的导航链接
在常规的导航栏中使用常用的图标，更多图标请参见[图标地址](http://www.runoob.com/bootstrap/bootstrap-glyphicons.html)

##### 代码：
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a href="#" class="navbar-brand">Apple 公司</a>
        </div>
        <ul class="nav navbar-nav navbar-right">
            <li><a href="#"><span class="glyphicon glyphicon-user"></span>注册</a></li>
            <li><a href="#"><span class="glyphicon glyphicon-log-in"></span>登录</a></li>
        </ul>
    </div>
</nav>
```

### 18.7 组件对齐方式

- 1.navbar-left：向左对齐导航栏中的元素
- 2.navbar-right：向右对齐导航栏中的元素

### 18.8 固定到顶部(navbar-fixed-top)
Bootstrap导航栏可以动态定位。导航栏固定在顶部，让它成为随着页面一起滚动的静态导航栏。使用class .navbar-fixed-top。如：\<nav class="navbar navbar-default navbar-fixed-top" role="navigation"\>

### 18.9 固定到底部(navbar-fixed-bottom)
使用class .navbar-fixed-bottom来让导航栏固定在页面底部

### 18.10 静态的顶部(navbar-static-top)
使用class .navbar-static-top，创建随着页面一起滚动的导航栏

### 18.11 反色的导航栏(navbar-inverse)
使用class .navbar-inverse创建一个带有黑色背景白色文本的反色导航栏

## 19. Bootstrap 面包屑导航(Breadcrumbs)
Bootstrap面包屑导航是一个简单的带有.breadcrumb class无序列表

##### 代码:
```html
<ul class="breadcrumb">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">2018</a></li>
    <li><a href="#">03</a></li>
    <li><a href="#">17</a></li>
</ul>
```

## 20. Bootstrap 分页
Bootstrap提供多个处理分页的class

- 1.pagination: 添加该class来在页面上显示分页
- 2.disabled: 定义当前链接不可点
- 3.active: 定义当前链接激活
- 4.pagination-lg(pagination-sm): 获取不同的大小项

### 20.1 默认的分页(pagination)
使用pagination来实现分页

##### 代码:
```html
<ul class="pagination">
    <li><a href="#">&laquo;</a></li>
    <li class="active"><a href="#">1</a></li>
    <li class="disabled"><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">&raquo;</a></li>
</ul>
```

### 20.2 分页的状态(disabled、active)
 disabled禁用当前链接，active激活当前链接。代码如上
 
### 20.3 分页的大小(pagination-lg)
使用pagination-lg将会放大当前链接。使用代码:\<ul class="pagination pagination-lg"\>

### 20.4 翻页(pager)
如果只想提供上一页／下一页，使用翻页就能满足。

- 1.pager: 添加该class来获得翻页链接
- 2.previous：把链接向左对齐
- 3.next：把链接向右对齐
- 4.disabled: 禁用当前链接

##### 代码：
```html
<ul class="pager">
    <li class="previous disabled"><a href="#">&larr; Older</a></li>
    <li class="next"><a href="#">Newer &rarr;</a></li>
</ul>
```

## 21. Bootstrap 标签(label)
使用class .label来显示标签。标签可用于计数、提示和页面上其他的标记显示

- 1.label label-default: 默认的灰色按钮
- 2.label label-primary: 蓝色按钮
- 3.label label-success: 绿色按钮

##### 代码:
```html
<span class="label label-default">默认标签</span>
<span class="label label-primary">主要标签</span>
<span class="label label-success">成功标签</span>
<span class="label label-info">信息标签</span>
<span class="label label-warning">警告标签</span>
<span class="label label-danger">危险标签</span>
```

## 22. Bootstrap 徽章(Badges)
徽章和标签相似，主要区别是徽章的边角更加圆滑。徽章常被用于突出显示新的或未读的项

##### 代码：
```html
<div class="container">
    <h2>徽章</h2>
    <p>
        <a href="#">收件箱<span class="badge">3</span></a>
    </p>
</div>
```

### 22.1 激活导航状态
可以将徽章放置在导航表中

##### 代码：
```html
<ul class="nav nav-pills">
    <li class="active"><a href="#">好友数目<span class="badge">3</span></a></li>
    <li><a href="#">请求加您为好友<span class="badge">10</span></a></li>
</ul>
```

## 23. Bootstrap 超大屏幕(jumbotron)
超大屏幕可以增加标题的大小，并为登陆页面内容添加更多的外边距。使用步骤如下:

- 1.创建一个带有class .jumbotron的容器\<div\>
- 2.除了更大的\<h1\>，字体粗细font-weight被减为200

##### 代码:
```html
<div class="container">
    <div class="jumbotron">
        <h1>欢迎登陆页面</h1>
        <p>这是一个超大屏幕(jumbotron)的实例</p>
        <p><a class="btn btn-info btn-lg" role="button">学习更多</a></p>
    </div>
</div>
```

### 23.1 非圆角页面
为了占用全部宽度且不带圆角的超大屏幕，请在class .container外使用class .jumbotron

##### 代码:
```html
<div class="jumbotron">
    <div class="container">
        <h1>欢迎登陆页面</h1>
        <p>这是一个超大屏幕(jumbotron)的实例</p>
        <p><a class="btn btn-info btn-lg" role="button">学习更多</a></p>
    </div>
</div>
```

## 24. Bootstrap 页面标题(page-header)
当一个网页中有多个标题且每个标题之间需要添加一定的间距时，页面标题这个功能就特别有用。

##### 代码：
```html
<div class="page-header">
    <h1>
        页面标题实例
        <small>子标题</small>
    </h1>
</div>
<p>内容部分</p>
```

## 25. Bootstrap 缩略图(thumbnail)
Bootstrap使用缩略图可为大多数站点中布局图像、视频、文本等。具体步骤如下:

- 1.在图像周围添加带有class .thumbnail的\<a\>标签
- 2.这会添加四个像素的内边距(padding)和一个灰色按钮
- 3.当鼠标悬停在图像上，会动画的显示出图像的轮廓

##### 代码:
```html
<div class="row">
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="http://www.runoob.com/wp-content/uploads/2014/06/kittens.jpg" alt="占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="http://www.runoob.com/wp-content/uploads/2014/06/kittens.jpg" alt="占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="http://www.runoob.com/wp-content/uploads/2014/06/kittens.jpg" alt="占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="http://www.runoob.com/wp-content/uploads/2014/06/kittens.jpg" alt="占位符缩略图">
        </a>
    </div>
</div>
```

### 25.1 添加自定义内容
可以向缩略图中添加各种HTML内容，比如标题、段落和按钮。具体步骤如下:

- 1.添加class .thumbnail的\<div\>
- 2.在\<div\>内，添加任何想要添加的东西

##### 代码:
```html
<div class="row">
    <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <img src="http://www.runoob.com/wp-content/uploads/2014/06/kittens.jpg">
            <div class="caption">
                <h3>缩略图标签</h3>
                <p>一些文本</p>
                <p>
                    <a href="#" class="btn btn-primary" role="button">按钮</a>
                    <a href="#" class="btn btn-default" role="button">按钮</a>
                </p>
            </div>
        </div>
    </div>
</div>
```

## 26. Bootstrap 警告(alerts)
警告向用户提供了一种定义消息样式的方式。

- 1.alert alert-success - 告警成功提示
- 2.alert alert-info - 告警信息提示
- 3.alert alert-warning - 警告提示
- 4.alert alert-danger - 危险提示

##### 代码:
```html
<div class="alert alert-success">成功！很好地完成了提交</div>
<div class="alert alert-info">信息！请注意这个信息</div>
<div class="alert alert-warning">警告！请不要提交</div>
<div class="alert alert-danger">错误！请进行一些更改</div>
```

### 26.1 可取消的警告(alert-dismissable)
创建一个可取消的警告步骤:

- 1.创建一个\<div\>，并向其添加一个class .alert和class .alter-success
- 2.向上面的\<div\>添加可选.alert-dismissable
- 3.添加一个关闭按钮

##### 代码:
```html
<div class="alert alert-success alert-dismissable">
    <button type="button" class="close" data-dismiss="alert" aria-hidden="true">
        &times;
    </button>
    成功！很好地完成了提交
</div>
```

### 26.2 警告(alert)中的链接
在警告中创建链接的步骤：

- 1.创建一个\<div\>，并向其添加class .alert和class .alert-success
- 2.使用class .alert-link来提供带有匹配颜色的链接

##### 代码:
```html
 <div class="alert alert-info">
    <a href="#" class="alert-link">
        信息！请注意这个信息
    </a>
</div>
```

## 27. Bootstrap 进度条
使用Bootstrap创建加载、重定向或动作状态的进步条

### 27.1 默认的进度条
创建一个基本的进度条的步骤:

- 1.添加一个带有class .progress的\<div\>
- 2.添加一个带有class .progress-bar的空的\<div\>
- 3.添加带有百分比的宽度的style属性，如style="width:60%"

##### 代码:
```html
<div class="progress">
    <div class="progress-bar" role="progressbar" aria-valuenow="40"
         aria-valuemin="0" aria-valuemax="100" style="width:40%">
         <span class="sr-only">40%完成</span>
    </div>
</div>
```

### 27.2 交替进度条
使用class .progress-bar-*属性来设置进度条的颜色

- 1.progress-bar-success - 成功颜色
- 2.progress-bar-info - 信息颜色
- 3.progress-bar-warning - 警告颜色
- 4.progress-bar-danger - 危险颜色

##### 代码:
```html
<div class="progress">
    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="40"
         aria-valuemin="0" aria-valuemax="100" style="width:40%">
         <span class="sr-only">40%完成</span>
    </div>
</div>
```

### 27.3 条纹的进度条(progress-striped)
使用属性class .progress-striped来创建进度条

##### 代码:
```html
<div class="progress progress-striped">
    <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="40"
         aria-valuemin="0" aria-valuemax="100" style="width:40%">
         <span class="sr-only">40%完成</span>
    </div>
</div>
```

### 27.4 动画的进度条(active)
在一个带有class .progress和class .progress-striped的\<div\>中。同时添加class .active属性，如:\<div class="progress progress-striped active"\>

### 27.5 堆叠进度条
将多个进度条放在相同的.progress中即可实现堆叠

##### 代码：
```html
<div class="progress progress-striped active">
    <div class="progress-bar progress-bar-info" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width:40%">
        <span class="sr-only">40% 完成</span>
    </div>
    <div class="progress-bar progress-bar-success" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width:30%">
        <span class="sr-only">40% 完成</span>
    </div>
    <div class="progress-bar progress-bar-danger" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width:20%">
        <span class="sr-only">40% 完成</span>
    </div>
</div>
```

## 28. Bootstrap 多媒体对象(media)
使用class .media来设计轻量级的媒体，有下列两个标签:

- 1.media：该class允许多媒体(图像、视屏、音频)浮动到内容区块的左边(meida-left)或右边(media-right)

##### 代码:
```html
<div class="media">
    <a class="media-left" href="#">
        <img class="media-object" src="http://avatar.csdn.net/F/7/8/3_thinking_fioa.jpg"
             alt="媒体对象">
    </a>
    <div class="media-body">
        <h4 class="media-heading">媒体标题</h4>
        <span>
            示例文本
        </span>
    </div>
</div>
```

## 29. Bootstrap 列表组(list-group)
列表组件用于以列表形式呈现复杂和自定义的内容。基本的列表组的步骤如下:

- 1.向元素\<ul\>添加class .list-group
- 2.向\<li\>添加class .list-group-item

##### 代码:
```html
<ul class="list-group col-md-3">
    <li class="list-group-item">thinking_fioa</li>
    <li class="list-group-item">ppp</li>
    <li class="list-group-item">luweilin</li>
</ul>
```

### 29.1 向列表组添加徽章(badge)
向\<li\>元素中添加\<span class="badge"\>即可添加徽章。会自动定位到右边

##### 代码:
```html
<ul class="list-group col-md-3">
    <li class="list-group-item">
        <span class="badge">新</span>
            thinking_fioa</li>
    <li class="list-group-item">ppp</li>
    <li class="list-group-item">luweilin</li>
</ul>
```

### 29.2 向列表组添加链接
使用\<a\>来添加链接

##### 代码:
```html
<div class="col-sm-3">
    <a href="#" class="list-group-item active">
        thinking_fioa
        <span class="badge">帅哥</span>
    </a>
    <a href="#" class="list-group-item">ppp</a>
    <a href="#" class="list-group-item">luweilin</a>
</div>
```

## 30. Bootstrap 面板(panel)
面板控件用于把DOM组件插入到一个盒子中。需要使用class .panel和class .panel-default

##### 代码:
```html
<div class="panel panel-default">
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
```

### 30.1 面板标题(panel-title)
可以使用两种方式来添加面板标题:

- 1.panel-heading - 向面板添加标题容器
- 2.使用.panel-title的\<h1\>和\<h6\>添加预定义样式的标题

##### 代码:
```html
<div class="panel panel-default">
    <div class="panel-heading">
        不带title的面板标题
    </div>
    <div class="panel-body">
        面板内容
    </div>
</div>
<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">
            带有title的面板标题
        </h3>
    </div>
    <div class="panel-body">
        面板内容
    </div>
</div>
```

### 30.2 面板脚注(panel-footer)
使用属性class .panel-footer来添加面板脚注

##### 代码:
```html
<div class="panel-footer">面板脚注</div>
```

### 30.3 带语境色彩的面板
设置语境色彩的面板有: panel-primary、panel-success、panel-info、panel-warning和panel-danger

### 30.4 带表格的面板
在面板中使用class .table来创建一个无边框的表格

##### 代码:
```html
<div class="panel panel-default col-md-6">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本面板
    </div>
    <table class="table">
        <tr>
            <th>姓名</th><th>年龄</th>
        </tr>
        <tr>
            <td>luweilin</td><td>24</td>
        </tr>
        <tr>
            <td>ppp</td><td>25</td>
        </tr>
    </table>
</div>
```

### 30.5 带列表组的面板
##### 代码:
```html
<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        一个基本面板内容
    </div>
    <ul class="list-group">
        <li class="list-group-item">thinking_fioa</li>
        <li class="list-group-item">luweilin</li>
        <li class="list-group-item">ppp</li>
    </ul>
</div>
```

## 31. Bootstrap Well
Well会让背景色片灰白，看起来达到凹陷的效果。使用class .well属性即可

### 31.1 尺寸大小(well-lg、well-sm)

- 1.well-lg:尺寸大
- 2.well-sm:尺寸小















