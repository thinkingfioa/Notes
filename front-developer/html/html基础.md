# HTML基础
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习html的网址是：http://www.runoob.com/html/html-intro.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/html
```
---

## 1 HTML简介

### 1.1 最简单的基本结构
- 1. \<html>标签下有：\<head>\</head>、\<body>\</body>两个部分
- 2. \<meat charset="utf-8">让页面显示中文不会出错
- 3. 只有\<body>内容才会在网页上显示

##### 代码：
```html
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8"> 
<title>页面标题</title>
</head>

<body> 
<p>我的第一个段落。</p>
</body>

</html>
```

## 2 HTML基础

### 2.1 HTML标题
HTML标题通过\<h1>-\<h6>标签定义的
#####代码：
```html
<h1>一级标题</h1>
<h2>二级标题</h2>
```

### 2.2 HTML段落
HTML段落通过\<p>标签定义
##### 代码:
```html
<p>第一个段落</p>
<p>第二个段落</p>
```

### 2.3 HTML链接
HTML链接通过\<a>标签定义的
##### 代码:
```html
<a href="http://www.baidu.com">链接百度</a>
```

### 2.4 HTML图像
HTML图像通过\<img>标签定义
##### 代码:
```html
<img src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" width="256" height="39"/>
```

## 3 HTML元素
### 3.1 HTML元素
HTML元素比较多，有开始标签和闭合标签。比如，段落标签中\<p>是开始标签，\</p>为结束标签

### 3.2 HTML元素语法
- 1. HTML元素以**开始标签**起始
- 2. HTML元素以**结束标签**终止
- 3. 元素的内容是开始标签和结束标签之间的内容
- 4. 某些HTML元素具有**空内容**，比如换行标签:\<br/>
- 5. 大多数HTML元素可拥有属性

### 3.3 HTML提示：使用小写标签
HTML标签不区分大小写，但是推荐使用小写字母。

## 4 HTML属性
属性是HTML元素的附加信息
### 4.1 HTML属性
- 1. HTML元素可是设置属性
- 2. 属性可以在元素中添加附加信息
- 3. 属性一般描述在**开始标签**中

##### 代码：
```html
<a href="http://www.baidu.com">百度链接</a>
```
### 4.2 HTML提示：使用小写属性
HTML属性也是不区分大小写，但是推荐使用小写属性

### 4.3 HTML属性手册
大多数HTML元素都适用的属性

|属性|描述|
|:---:|:---:|
|class|为html元素定义一个或多个类名(类名将从文件中引入)|
|id|定义元素的唯一id|
|style|规定元素的行内样式|
|title|描述元素的额外信息|

## 5 HTML标题
- 1. HTML标题是通过元素\<h1>-\<h6>定义，大小一次递减
- 2. 1到6号标题与1到6号字体逆序对应

##### 代码：
```html
<h1>1号标题</h1>
<font size="6">6号字体文本</font>
```

### 5.1 HTML水平线
\<hr>标签在HTML页面中创建水平线

##### 代码:
```html
<body>
	<h3>3级标题</h3>
	<p>hr 标签定义水平线: </p>
	<hr />
</body>
```

### 5.2 HTML注释
\<!-- 注释 -->用于代码注释

## 6 HTML段落
- 1. 段落通过\<p>标签定义的。且浏览器会在\<p>后加上**折行+空行**
- 2. HTML代码中添加额外的空行和换行都是无用的。只能通过HTML标签才能进行排版

### 6.1 HTML折行
折行通过\<br/>标签定义的。

##### 代码:
```html
<body>
	<p>第一个段落</p>
	<p>第二个段落</p>
	<p>第三个段落</p>
	<hr>
	<p>
		第一个段落<br/>第二个段落<br/>第三个段落<br/>
	</p>
</body>
```

## 7 HTML文本格式化
|标签|描述|
|:---:|:---:|
|\<b>|定义粗体文本|
|\<em>|定义着重文字|
|\<i>|定义斜体|
|\<small>|定义小号字|
|\<strong>|定义加重语气|
|\<sub>|定义下标字|
|\<sup>|定义上标字|
|\<ins>|定义下划线|
|\<del>|定义删除字|

##### 代码：
```html
<body>
	<b>粗体</b><br/>
	<em>着重文字</em><br/>
	<i>斜体</i><br/>
	<small>小号字</small><br/>
	<strong>加重语气</strong><br/>
	<sub>下标字</sub><br/>
	<sup>上标字</sup><br/>
	<ins>下划线</ins><br/>
	<del>删除字</del><br/>
</body>
```

## 8 HTML链接
HTML使用标签\<a>来设置超文本链接。超链接可以是文字或图片。

### 8.1 HTML链接-target属性
使用target可以定义被链接的文档在新窗口中打开

##### 代码:
```html
<body>
	<a href="http://github.com/thinkingfioa" target="_blank">新窗口打开gitHub主页</a>
</body>
```

### 8.2 HTML链接-id属性
id属性用于创建一个HTML文档书签标记。可以利用id属性实现页面内的跳转

##### 代码:
```html
<body>
	<a href="#tips">跳转到下一页地方</a><br/>
	<a id="tips">下一页</a>
</body>
```

### 8.3 HTML链接注意事项-有用提示
请始终将正斜杠添加到子文件夹上，否则会产生两次HTTP请求。如：href="http://www.runoob.com/html/"

### 8.4 HTML图片链接
链接标签\<a>也可以用图片来作为内容

##### 代码：
```html
<body>
	<span>图片链接跳转</span>
	<a href="http://github.com/thinkingfioa/" target="_blank">
		<img src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" border="0" width="32" height="32">
	</a>
</body>
```

## 9 HTML头部
- 1. \<head>元素包含了所有头部标签元素。在<head>元素中，可以插入脚本(scripts)、样本(CSS)、及各种meta信息。
- 2. 头部区域的元素标签：\<title>、\<style>、\<meta>、\<link>、\<script>、\<base>

### 9.1 HTML \<base>元素
\<base>标签描述基本的链接地址／链接目标。如果链接前面没有http，该标签会补充到文档所有链接地址上。

##### 代码：
```html
<head>
<meta charset="utf-8">
<title>THML文本格式化</title>
<base href="https://avatars1.githubusercontent.com/u/" target="_blank">
</head>
<body>
	<span>图片链接跳转</span>
	<a href="http://github.com/thinkingfioa" target="_blank">
		<img src="13462500?s=460&v=4" border="0" width="32" height="32">
	</a>
</body>
```

### 9.2 HTML \<link>元素
\<link>标签通常被用于链接到样式表。引入样式表，

##### 代码:
```html
<head>
	<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

### 9.3 HTML \<style>元素
\<style>标签定义HTML文档的样式

##### 代码:
```html
<head>
	<style type="text/css">
		body{
			background-color:yellow
		}
		p{
			color:blue
		}
	</style>
</head>
```

### 9.4 HTML \<script>元素
\<script>标签用于加载脚本文件，如:javaScript

## 10 HTML CSS
CSS可以通过以下方式添加到HTML中:

- 1. 内联样式-在HTML元素中使用"style"属性
- 2. 内部样式表-在HTML文档头部\<head>区域使用\<style>元素
- 3. 外部引用-使用标签\<link>来引入外部CSS文件。


### 10.1 内联样式
当个别元素需要特殊样式时，使用内联样式。在对应的标签中使用样式属性即可,多个属性之间用分号';'分割.

##### 代码:
```html
<body>
	<p style="background-color: red;margin-left: 20px;">一个段落标签style设置</p>
</body>
```

#### 10.1.1 HTML样式实例-字体、字体颜色、字体大小和本文对其方式
- 1. 使用font-family(字体）、color(字体颜色)和font-size(字体大小)属性定义字体的样式
- 2. 使用text-align(文字对齐)

##### 代码:
```html
<body>
	<p style="font-family: arial;color:red;font-size=20px;">字体-红色-20大小</p>
	<p style="text-align: center">文字居中显示</p>
</body>
```

### 10.2 内部样式表
当单个文件需要特别样式时，使用内部样式表。在\<head>标签中定义属性

##### 代码:
```html
<style type="text/css">
	body{
		background-color: yellow;
	}
	p{
		color:green;
	}
</style>
```

### 10.3 外部样式表
 当样式需要被应用到多个页面的时候，外部样式表是理想的选择。对样式进行统一管理.
 
##### 代码:
```html
<link rel="stylesheet" type="text/css" href="mystyle.css">
```

## 11 HTML图像
HTML中使用\<img>定义图像

- 1. \<img>是空标签，意思是，它只包含属性，并且没有闭合标签
- 2. src是源属性，用于指定该图像所在的位置
- 3. \<map>标签定义图像地图，实现图像映射
- 4. \<area>标签定义图像地图，标记图像映射的具体区域

### 11.1 HTML图像-属性
- 1. alt属性用来为图片定义一串预备的可替换的文本。当浏览器无法加载图像时，显示替换文本
- 2. height(高度)和width(宽度)属性用来设置图像的宽度和高度
- 3. border(边框)用来为图像加上边框,如:border="10"

##### 代码：
```html
<body>
	<img src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" alt="头像无法显示" width="32" height="32" style="float:right;">
</body>
```

## 12 HTML表格
HTML中使用\<table>标签定义表格，数据单元可以包含文本、图片、表单等等。

### 12.1 HTML表格属性介绍
- 1. \<caption>定义表格标题
- 2. \<tr>(table row)定义表的一行
- 3. \<th>(table head)用来定义表头
- 4. \<td>(table data)定义表的数据部分
- 5. border属性定义表格边框粗细

##### 代码:
```html
<body>
	<table border="1">
		<caption style="font-size: 20px;color: red;"><b>傻逼名单</b></caption>
		<tr style="color:green;">
			<th>号</th>
			<th>姓名</th>
			<th>年纪</th>
		</tr>
		<tr>
			<td>1</td>
			<td>ppp</td>
			<td>26</td>
		</tr>
		<tr>
			<td>2</td>
			<td>lwl</td>
			<td>24</td>
		</tr>
	</table>
</body>
```

### 12.2 表格跨行或跨列的表格单元格
- 1. colspan属性用于单元格跨行单元格
- 2. rowspan属性用于单元格跨列单元格

##### 代码:
```html
<!-- 跨行单元格 -->
	<table border="1">
		<caption>男女朋友关系</caption>
		<tr>
			<th>号</th>
			<th colspan="2">姓名</th>
		</tr>
		<tr>
			<td>1</td>
			<td>lwl</td>
			<td>ppp</td>
		</tr>
		<tr>
			<td>2</td>
			<td>sunzibo</td>
			<td>wcf</td>
		</tr>
	</table>

	<!-- 跨列单元格 -->
	<table border="1">
		<caption>男女朋友关系</caption>
		<tr>
			<th>号</th>
			<td>1     </td>
		</tr>
		<tr>
			<th rowspan="2">姓名</th>
			<td>sunzibo</td>
			<td>wcf</td>
		</tr>
	</table>
```

## 13 HTML列表
- 1. 标签\<ul>(unorder list>用于无序标签
- 2. 标签\<ol>(order list>用于有序标签
- 3. 标签\<li>列表

##### 代码:
```html
<body>
	<h4>无序列表</h4>
	<ul>
		<li>Coffee</li>
		<li>Tea</li>
		<li>Milk</li>
	</ul>
	<h4>有序列表</h4>
	<ol>
		<li>Coffee</li>
		<li>Tea</li>
		<li>Milk</li>
	</ol>
</body>
```

### 13.1 HTML无序列表

### 13.2 HTML有序列表

























