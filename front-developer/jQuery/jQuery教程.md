# 一、jQuery 教程
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
jQuery是一个JavaScript库，极大的简化了JavaScript编程。
学习html的网址是：http://www.runoob.com/jquery/jquery-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/jQuery 
```
---

## 1. jQuery简介
jQuery库可以通过一行简单的标记被添加到网页中
### 1.1 什么是jQuery
jQuery是一个JavaScript函数库，是一个轻量级的"写的少，做的多"的JavaScript库。jQuery库包含以下功能，除此之外，jQuery还提供大量的插件:

- 1.HTML元素获取
- 2.HTML元素操作
- 3.CSS操作
- 4.HTML事件函数
- 5.JavaScript特效和动画
- 6.HTML-DOM遍历和修改
- 7.AJAX
- 8.Utilities

## 2. jQuery安装
可以通过两种方法在网页中添加jQuery，如下:

- 1.从[jquery.com](http://jquery.com/download/)下载jQuery库
- 2.从CDN中加载jQuery，如百度、谷歌等大公司

### 2.1 下载jQuery
jQuery提供两个版本:

- 1.Production version-用于实际的网站，已被精简和压缩，后缀名为: .min.js
- 2.Development version-用于测试和开发(未压缩，可读)，后缀名为: .js

##### 代码:
```html
<head>
	<script src="./src/jquery-3.2.1.min.js"><script>
</head>
```

### 2.2 CDN获取jQuery
如果不希望下载并存放jQuery，可以通过CDN引用它。百度、谷歌和新浪等公司都有对外开放
##### 代码:
```html
<head>
	<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
</head>
```

### 2.3 案例理解
```html
<head>
    <meta charset="UTF-8">
    <title>jQuery教程</title>
    <script src="./js/jquery-3.2.1.min.js"></script>
</head>
<body>
    <p>如果点我，我就消失!</p>
    <p>继续点我</p>
    <p>接着点我</p>
    <script>
        $(document).ready(function () {
            $("p").click(function () {
                $(this).hide();
            });
        });
    </script>
</body>
```

## 3. jQuery语法
通过jQuery，可以选取(query)HTML元素，并对他们执行"操作"(actions)

### 3.1 jQuery语法
jQuery语法是通过选取HTML元素，并对选取的元素执行某些操作。基础语法: \$(selector).action()

- 1.美元符号定义jQuery
- 2.选择符(selector)"查询"和"查找"HTML元素
- 3.jQuery的action()执行对元素的操作

实例:

- 1.$(this).hide()-隐藏当前元素
- 2.$("p").hide()-隐藏所有\<p>元素
- 3.$("p.test").hide()-隐藏所有class="test"的\<p>元素
- 4.$("#test").hide()-隐藏所有id="test"的元素
- 5.$("ul li-first").hide()-隐藏第一个\<ul>元素的第一个\<li>元素
- 6.$("ul li-first-child").hide()-隐藏每个\<ul>元素的第一个\<li>元素
- 7.$("a[target='\_blank']")-选取所有target属性值等于"\_blank"的\<a>元素

### 3.2 文档就绪事件
本篇实例中的所有jQuery函数位于一个document ready函数

##### 代码:
```html
$(document).ready(function(){
	//开始写 jQuery代码...
});
```
##### 代码解释:
上述代码为了防止文档在完全加载(就绪)之前运行jQuery代码，也就是DOM加载完成后才对DOM进行操作。
##### 简洁代码写法:
```html
$(function(){
	// 开始写jQuery代码...
});
```

## 4. jQuery 选择器
jQuery 选择器允许你对HTML元素组或单个元素进行操作

### 4.1 jQuery 选择器
- 1.jQuery选择器基于元素的id、类、类型、属性和属性值等"查找"HTML元素。
- 2.jQuery中所有选择器都是以美元符号开头:$()

### 4.2 元素选择器
jQuery元素选择器基于元素名选取元素，如页面中所有\<p>元素，则为: \$("p")
#####代码:
```html
<body>
    <h2>这是一个标题</h2>
    <div>
        <span>这是一个段落</span><br/>
        <span>这是另一个段落</span><br/>
    </div>
    <button>点我</button>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
               $("div").hide();
            });
        });
    </script>
</body>
```

### 4.3 #id 选择器
页面中元素的id应该是唯一的，所以在页面中选取唯一的元素需要通过#id 选择器。#id 选择器通过HTML元素提供的id属性来指定页面的元素
##### 代码:
```html
<body>
    <h2>这是一个标题</h2>
    <div>
        <span>这是一个段落</span><br/>
        <span id="span1">这是另一个段落</span><br/>
    </div>
    <button id="mybut1">点我隐藏一个</button>
    <script>
        $(document).ready(function () {
            $("#mybut1").click(function () {
                $("#span1").hide();
            })
        });
    </script>
</body>
```

### 4.4 .class 选择器
jQuery类选择器可以通过指定的class查找元素
##### 代码:
```html
<body>
    <h2>这是一个标题</h2>
    <div>
        <span>这是一个段落</span><br/>
        <span class="span1">这是另一个段落</span><br/>
    </div>
    <button id="mybut1">点我隐藏一个</button>
    <script>
        $(document).ready(function () {
            $("#mybut1").click(function () {
                $(".span1").hide();
            })
        });
    </script>
</body>
```

### 4.5 \$("ul li:first")选择器
选取第一个\<ul>元素的第一个\<li>元素
##### 代码:
```html
<body>
    <ul>
        <li>Coffee</li>
        <li>Tea</li>
        <li>Coca Cola</li>
    </ul>
    <button>隐藏列表第一个</button>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
               $("ul li:first").hide();
            });
        });
    </script>
</body>
```

### 4.5 更多的选择器
|语法|描述|
|:---:|:---:|
|\$("*")|选取所有元素|
|\$(this)|选取当前HTML元素|
|\$("p.className")|选取class为className的\<p>元素|
|\$("p:first")|选取第一个\<p>元素|
|\$("ul li:first")|选取第一个\<ul>元素的第一个\<li>元素|
|\$("ul li:first-child")|选取每个\<ul>元素的第一个\<li>元素|
|\$("[href]")|选取带有href属性的元素|
|\$("a[target='\_blank']")|选取所有target属性值等于"\_blank"的\<a>元素|
|\$("a[target!='\_blank']")|选取所有target属性值不等于"\_blank"的\<a>元素|
|\$(":button")|选取所有type="button"的\<input>元素和\<button>元素|
|\$("tr:even")|选取偶数位置的\<tr>元素|
|\$("tr:odd")|选取奇数位置的\<tr>元素|

### 4.6 理解
- 1.":"可以理解为种类，如 "tr:even"表格中偶数行的种类
- 2."[]"理解为属性，如"a[target="\_blank"]表示元素\<a>中有属性"\_blank"

## 5 jQuery事件


# 二、jQuery效果


















