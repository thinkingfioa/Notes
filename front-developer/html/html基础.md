# HTML基础
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习html的网址是：http://www.runoob.com/html/html-intro.html
gitHub地址: https://github.com/thinkingfioa
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
<font size="6>6号字体文本</font>
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
	<a href="http://github.com/thinkingfioa" target="_blank">
		<img src="https://avatars1.githubusercontent.com/u/13462500?s=460&v=4" border="0" width="32" height="32">
	</a>
</body>
```

### 9 HTML头部












