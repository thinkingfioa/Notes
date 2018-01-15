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

## 5. jQuery 事件
 页面对于不同访问者的响应叫做事件，事件处理程序指的是当HTML中某些事件发生时调用的方法
 
 - 1.在元素上移动鼠标
 - 2.选取单选按钮
 - 3.点击元素

### 5.1 jQuery 事件方法语法
```html
$("p").click(function(){
	// 事件触发后执行对应代码
});
```

### 5.2 常用的jQuery事件方法

#### 5.2.1 \$(document).ready()
\$(document).ready()方法允许在文档完全加载完后执行函数。保证安全性

#### 5.2.2 click()
click()方法是当按钮点击事件被触发时会调用的一个函数，上面的代码有很多

#### 5.2.3 dblclick()
当双击元素时，发生dblclick事件
##### 代码:
```html
<body>
    <p>我要消失</p>
    <button id="MyButton">请消失</button>
    <script>
        $(document).ready(function () {
           $("#MyButton").dblclick(function () {
               $("p").hide();
           });
        });
    </script>
</body>
```

#### 5.2.4 hover()事件
hover()方法用于模拟光标悬停事件。当鼠标移到元素上，触发第一个函数(mouseenter)；当鼠标移开元素时，触发第二个函数(mouseleave)
##### 代码:
```html
<body>
    <p class="myP" style="width: 400px">这是一个段落</p>
    <script>
        $(document).ready(function(){
            $("p.myP").hover(
                function(){
                    window.alert("进入p1(这是一个段落)");
                },
                function () {
                    window.alert("离开p1(这是一个段落)");
                }
            );
        });
    </script>
</body>
```

#### 5.2.5 focus()事件
元素获得焦点，发生focus()事件。元素失去焦点，发生blur()事件
##### 代码:
```html
<body>
    <span>First Name:</span>
    <input type="text" name="firstName"><br/>
    <span>Last Name:</span>
    <input type="text" name="lastName"><br/>
    <script>
        $(document).ready(function () {
            $("input").focus(function () {
                $(this).css("background-color", "red");
            });
            $("input").blur(function () {
                $(this).css("background-color", "green");
            });
        });
    </script>
</body>
```

#### 5.2.4 其他常用事件
|事件|效果|
|:---:|:---:|
|mouseenter()|鼠标穿过元素时，发生mouseenter事件|
|mouseleave()|鼠标离开元素时，发生mouseleave事件|
|mousedown()|鼠标移动到元素上方，并按下鼠标按键时，发生|
|mouseup()|在元素上松开鼠标按钮时，会发生|
|blur()|元素失去焦点时，发生blur事件|



# 二、jQuery效果

## 6. jQuery-隐藏和显示

### 6.1 jQuery hide()和show()
- 1.使用hide()方法和show()方法来隐藏和显示HTML元素
- 2.\(selector).hide(speed,callback)方法表明，可以通过speed来指定隐藏速度

##### 代码:
```html
<body>
    <p>点击"隐藏"则隐藏，点击"显示"就显示</p>
    <button id="button1">隐藏</button>
    <button id="button2">显示</button>
    <script>
        $(document).ready(function(){
           $("#button1").click(function () {
               $("p").hide(100);
           });
           $("#button2").click(function(){
              $("p").show();
           });
        });
    </script>
</body>
```

### 6.2 jQuery toggle()
使用toggle()方法切换hide()和show()方法。
##### 代码:
```html
<body>
    <p>点击"隐藏"则隐藏，点击"显示"就显示</p>
    <button id="button3">一个按钮控制</button>
    <script>
        $(document).ready(function(){
           $("#button3").click(function () {
               $("p").toggle(1000);
           });
        });
    </script>
</body>
```

### 6.3 如何隐藏文本
##### 代码:
```html
<head>
    <style type="text/css">
        div.hide{
            background-color: #cc2e5c;
            padding:7px;
            border:solid 1px #cc7775;
        }
    </style>
</head>
<body>
    <h3>Google</h3>
    <div class="hide">
        <button class="myButton">点我隐藏</button>
        <p>站点名:Google</p>
        <p>站点URL: http://wwww.google.com</p>
    </div>
    <h3>thinkingfioa个人主页</h3>
    <div class="hide">
        <button class="myButton">点我隐藏</button>
        <p>站点名: thinkingfioa主页</p>
        <p>站点URL: https://github.com/thinkingfioa</p>
    </div>
    <script>
        $(document).ready(function () {
           $(".myButton").click(function(){
              $(this).parents(".hide").hide("slow");
           });
        });
    </script>
</body>
</html>
```

## 7. jQuery - 淡入淡出
通过jQuery可以实现元素的淡入淡出效果，jQuery拥有下面四种fade方法:

- 1.fadeIn() - 淡入已隐藏的元素
- 2.fadeOut() - 淡出可见的元素
- 3.fadeToggle() - 可以在fadeIn()方法与fadeOut()方法之间切换
- 4.fadeTo() - 允许渐变为给定的不透明度(值介于0与1之间)

### 7.1 jQuery fadeIn()方法
fadeIn()方法用于淡入已隐藏的元素，语法:\$(selector).fadeIn(speed, callback)
##### 代码:
```html
<body>
    <p>演示fadeIn()方法，渐入效果</p>
    <button>点击淡入div元素</button><br/>
    <div id="div1" style="width: 80px; height: 80px; background-color: #ff2c37; display: none;"></div><br>
    <div id="div2" style="width: 80px; height: 80px; background-color: #a5ff7e; display: none;"></div><br>
    <div id="div3" style="width: 80px; height: 80px; background-color: #396aff; display: none;"></div><br>
    <script>
        $(document).ready(function(){
           $("button").click(function(){
              $("#div1").fadeIn();
              $("#div2").fadeIn("slow");
              $("#div3").fadeIn(3000);
           });
        });
    </script>
</body>
```

### 7.2 fadeOut()方法
fadeOut()方法用于淡出可见元素，语法:\$(selector).fadeOut(speed, callback);
##### 代码:
```html
<script>
	$(document).ready(function(){
		$("button").click(function(){
			$("#div1").fadeOut();
			$("#div2").fadeOut("slow");
			$("#div3").fadeOut(3000);
		});
	});
</script>
```

### 7.3 fadeToggle()方法
可以在方法fadeIn()和方法fadeOut()之间切换

### 7.4 fadeTo()方法
fadeTo()方法允许渐变为给定的不透明度(值介于0-1之间)
##### 代码:
```html
<script>
	$(document).ready(function(){
		$("button").click(function(){
			$("#div1").fadeTo("slow", 0.15);
			$("#div2").fadeOut("slow", 0.4);
			$("#div3").fadeOut(3000, 0.7);
		});
	});
</script>
```

## 8. jQuery 滑动
滑动方法可使元素上下滑动

### 8.1 jQuery滑动方法
通过jQuery，可以在元素上创建滑动效果，jQuery拥有一下滑动方法:

- 1.slideDown() - 用于向下滑动元素
- 2.slideUp() - 用于向上滑动元素
- 3.slideToggle() - 可以在 slideDown() 与 slideUp() 方法之间进行切换





























