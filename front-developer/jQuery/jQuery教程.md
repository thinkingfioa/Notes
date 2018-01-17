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
- 5.$("ul li:first").hide()-隐藏第一个\<ul>元素的第一个\<li>元素
- 6.$("ul li:first-child").hide()-隐藏每个\<ul>元素的第一个\<li>元素
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

### 8.2 slideDown()方法
slideDown()方法用于向下滑动元素
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>jQuery教程</title>
    <script src="./js/jquery-3.2.1.min.js"></script>
    <style type="text/css">
        #flip,#panel{
            padding: 5px;
            text-align: center;
            background-color: #a5ff7e;
            border: solid 1px #c3c3c3;
        }
        #panel{
            padding:50px;
            display: none;
        }
    </style>
</head>
<body>
    <div id="flip">点我滑下面板</div>
    <div id="panel">Hello World!</div>
    <script>
        $(document).ready(function () {
           $("#flip").click(function () {
               $("#panel").slideDown("slow");
           })
        });
    </script>
</body>
```

### 8.3 slideUp()方法
slideUp()方法用于向上滑动元素
##### 代码:
```html
<script>
	$(document).ready(function(){
		$("#flip").click(function(){
			$("#panel").slideUp("slow");
		})
	});
<script>
```

### 8.4 slideToggle()方法
slideToggle()方法可以在 slideDown() 与 slideUp() 方法之间进行切换
##### 代码:
```html
<script>
	$(document).ready(function(){
		$("#flip").click(function(){
			$("#panel").slideToggle("slow");
		});
	});
</script>
```

## 9. jQuery 动画
jQuery animate()方法允许创建自定义动画

### 9.1 animate()方法
- 1.animate()方法用于创建自定义动画，语法:$(selector).animate({params}, speed, callback);，其中params时必填属性，通常是CSS属性
- 2.HTML元素默认是不可移动，如果需要改变，需要添加属性position，将其值设置为relative、fixed、或absolute

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>jQuery教程</title>
    <script src="./js/jquery-3.2.1.min.js"></script>
    <style type="text/css">
        #mydiv {
            background-color: #a5ff7e;
            height:100px;
            width:100px;
            position:absolute;
        }
    </style>
</head>
<body>
    <button>开始动画</button>
    <div id="mydiv"></div>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
               $("#mydiv").animate({left:"250px"})
            });
        });
    </script>
</body>
```

### 9.2 animate() - 操作多个属性
animate()方法可以传入多个参数
##### 代码:
```html
<script>
	$(document).ready(function () {
		$("button").click(function () {
			$("#mydiv").animate({
				left:"250px",
				width:"250px",
				height:"250px",
				opacity:'0.5',
			})
		});
	});
</script>
```

### 9.3 animate() - 使用相对值
可以使用+=或-=来定义相对值(该值相对于元素的当前值)
##### 代码:
```html
<script>
	$(document).ready(function(){
		$("button").click(function(){
			$("#mydiv").animate({
				left:"250px",
				height:"+=150px",
				width:"+=150px",
			});
		});
	});
</script>
```

### 9.4 animate() - 使用预定义的值
可以把属性的动画值设置为"show"、"hide"或"toggle":
##### 代码:
```html
$("button").click(function(){
	$("#mydiv").animate({
		height:"toggle",
	});
});
```

### 9.5 animate() - 使用队列功能
jQuery提供针对animate()方法的队列，可以写多个animate()方法，会依次以队列模式调用
##### 代码:
```html
<script>
	$(document).ready(function () {
		$("button").click(function () {
			$("#mydiv").animate({height:"+=200px", opacity: "0.5"}, "slow");
			$("#mydiv").animate({width:"+=200px", opacity: "0.8"}, "slow");
			$("#mydiv").animate({width:"-=200px", opacity:"0.5"}, "slow");
			$("#mydiv").animate({height:"-=200px", opacity:"1"}, "slow");
		});
	});
</script>
```

### 9.6 animate() - 改变文字大小
##### 代码:
```html
<script>
	$(document).ready(function () {
		$("button").click(function () {
			$("#mydiv").animate({height:"+=200px", opacity: "0.5"}, "slow");
			$("#mydiv").animate({width:"+=200px", opacity: "0.8"}, "slow");
			$("#mydiv").animate({fontSize:"3em"}, "slow");
		});
	});
</script>
```

## 10. jQuery 停止动画
jQuery提供stop()方法用于在动画或效果完成前对它们进行停止

### 10.1 stop()方法
- 1.stop()方法适用于所有jQuery效果函数，包括滑动、淡入淡出和自定义动画。语法:$(selector).stop(stopAll,goToEnd);
- 2.参数stopAll表示是否清除动画队列，默认是false;参数goToEnd规定是否立即完成当前动画，默认是false

##### 代码:
```html
$("stopButton").click(function(){
	$("#panel").stop();
});
```

## 11. jQuery Callback方法
Callback()方法在当前动画完成100%后执行

### 11.1 jQuery 动画的问题
 jQuery提供很多动画方法中，都提供callBack()方法入口，如hide()方法等。
##### 代码:
```html
<script>
	$(document).ready(function () {
		$("button").click(function () {
			$("div.myDiv").hide("slow", function () {
				window.alert("隐藏完毕");
			});
		});
	});
</script>
```

## 12. jQuery - 链(Chaining)
jQuery提供动作/方法链接在一起，Chaining允许我们在一条语法中运行多个jQuery方法

### 12.1 jQuery 方法链接
链接技术，允许我们在相同的元素上运行多条jQuery命令，一条接一条。如:\$("#p1").css("color","red").slideUp(2000).slideDown(2000);
##### 代码:
```html
<body>
    <div class="myDiv">
        <span>我知道有人偷偷喜欢我!</span>
    </div>
    <button>请开始你的表演</button>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
                $(".myDiv").css("color","red").slideUp(2000).slideDown(2000);
            });
        });
    </script>
</body>
```

# 三、 jQuery HTML

## 13. jQuery 捕获(获取内容和属性)
jQuery 拥有可操作HTML元素和属性的强大方法

### 13.1 获得内容 - text()、html()和val()
三个简单实用的用于DOM操作的jQuery方法:

- 1.text() - 设置或返回所选元素的文本内容
- 2.html() - 设置或返回所选元素的内容(包括HTML标记)，完成的HTML内容
- 3.val() - 设置或返回表单字段的值，也就是对应的value

##### 代码:
```html
<body>
    <div id="mydiv1">
        <span>这是段落中的<b>粗体</b></span>
    </div>
    <div>
        <span>姓名:</span>
        <input type="text" class="myname" name="name">
    </div>
    <button id="mybtn1">显示文本内容</button>
    <button id="mybtn2">显示HTML内容</button>
    <button id="mybtn3">显示字段值</button>
    <script>
        $(document).ready(function () {
           $("#mybtn1").click(function () {
               window.alert("显示:"+$("#mydiv1").text());
           });
           $("#mybtn2").click(function () {
               window.alert("显示:"+$("#mydiv1").html());
           });
           $("#mybtn3").click(function () {
               window.alert("显示:"+$(".myname").val());
           });
        });
    </script>
</body>
```

### 13.2 获取属性 - attr()
attr()方法用于获取属性值。
#### 代码:
```html
<body>
    <a href="https://github.com/thinkingfioa">thinkingfioa主页</a>
    <button id="mybtn">显示属性</button>
    <script>
        $(document).ready(function () {
           $("#mybtn").click(function () {
               window.alert("显示:"+$("a").attr("href"));
           });
        });
    </script>
</body>
```

## 14. jQuery 设置
jQuery提供方法修改元素内容和属性等

### 14.1 设置内容-text()、html()和val()
和13章节使用的方法同样，三个简单实用的用于DOM操作的jQuery方法:

- 1.text() - 设置或返回所选元素的文本内容
- 2.html() - 设置或返回所选元素的内容(包括HTML标记)，完成的HTML内容
- 3.val() - 设置或返回表单字段的值，也就是对应的value

##### 代码:
```html
<body>
    <p id="p1">这是一个段落</p>
    <p id="p2">这是第二个段落</p>
    <span>输入框:</span>
    <input type="text" id="myName" name="name" value="lwl"><br/>
    <button id="btn1">这是文本</button>
    <button id="btn2">设置HTML</button>
    <button id="btn3">设置value值</button>
    <script>
        $(document).ready(function () {
            $("#btn1").click(function () {
               $("#p1").text("hello")
            });
            $("#btn2").click(function () {
                $("#p2").html("<p>thinkingfioa</p>");
            });
            $("#btn3").click(function () {
                $("#myName").val("ppp");
            });
        });
    </script>
</body>
```

### 14.2 text()、html()和val()的回调函数
上面三个函数:text()、html()和val()拥有回调函数。回调函数第二个参数，是原始(旧的)值
##### 代码:
```html
$("#btn1").click(funcktion(){
	$("#test1").text(function(i,origText){
		return "旧文本: "+origText+", 新文本: panpingping");
	});
})
```

### 14.3 设置属性 - attr()
attr()用于设置/改变属性值，下列代码演示元素标签\<a>的两个属性:href, title的设置
##### 代码:
```html
<body>
    <a id = "aaa" href="https://github.com/thinkingfioa">thinkingfioa主页</a>
    <button id="btn">改变属性</button>
    <script>
        $(document).ready(function () {
            $("#btn").click(function () {
               $("#aaa").attr({"href" : "http://write.blog.csdn.net/postlist",
                                "title": "thinking_fioa的CSDN地址",
               });
                // 通过修改的 title 值来修改链接名称
               title =  $("#aaa").attr('title');
               $("#aaa").html(title);
            });
        });
    </script>
</body>
```

## 15. jQuery 添加元素
通过jQuery，可以很容易添加新元素/内容

### 15.1 添加新的HTML内容
用于添加新内容的四个jQuery方法:

- 1. append() - 在被选元素的**结尾**插入内容
- 2. prepend() - 在被选元素的开头插入内容
- 3. after() - 在被选元素**之后**插入内容
- 4. before() - 在被选元素之前插入内容 

### 15.2 jQuery append()方法
append()方法在元素的结尾插入内容。与after()方法完全不同，after()方法是在元素之后插入内容
##### 代码:
```html
<body>
    <p>这是一个段落</p>
    <p>这是另一个段落</p>
    <ul id="myUl">
        <li>List item 1</li>
        <li>List item 2</li>
        <li>List item 3</li>
    </ul>
    <button id="myBtn1">添加文本</button>
    <button id="myBtn2">添加列表项</button>
    <script>
        $(document).ready(function () {
            $("#myBtn1").click(function () {
                $("p").append(" <b>追加文本</b>");
            });
            $("#myBtn2").click(function () {
                $("ul").append("<li>List item 4</li>");
            });
        });
    </script>
</body>
```

### 15.3 jQuery prepend()方法
prepend()方法在被选元素开头插入内容
##### 代码:
```html
<script>
	$(document).ready(function () {
		$("#myBtn1").click(function () {
			$("p").prepend(" <b>追加文本</b>");
		});
		$("#myBtn2").click(function () {
			$("ul").prepend("<li>List item 4</li>");
		});
	});
</script>
```

### 15.4 jQuery - after()方法和before()方法
- 1.after()方法在被选元素之后插入内容
- 2.before()方法在被选元素之前插入内容
##### 代码:
```html
$("img").after("在后面加上文本");
$("img").before("在前面加上文本");
``` 

## 16. jQuery 删除元素
jQuery可以非常容易删除已有的HTML元素

### 16.1 删除元素/内容
jQuery提供两种方法删除元素:

- 1.remove() - 删除被选元素(及其子元素)
- 2.empty() - 从被选元素中删除子元素

### 16.2 jQuery remove()方法
remove()方法删除被选元素及其子元素
##### 代码:
```html
<body>
    <div id="myDiv" style="background-color: #ff2c37; height:100px; width:300px;padding:70px; border: 1px solid black;">
        <span>这是div中的文本</span><br/>
        <p>这是div中的一个段落</p>
        <p>这是div中的另一个段落</p>
    </div>
    <button>移除div元素</button>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
                $("#myDiv").remove();
            });
        });
    </script>
</body>
```

### 16.3 jQuery empty()方法
empty()方法删除被选元素的子元素
##### 代码:
```html
$("button").click(function(){
	$("#myDiv").empty();
});
```

### 16.4 过滤被删除的元素
remove()方法可以传入一个参数，允许对被删除元素过滤，如:\$("p").remove(".italic")表示移除class="italic"

## 17. jQuery CSS类
通过jQuery可以非常容易的对CSS元素进行操作，有如下4种操作CSS方法:

- 1.addClass() - 向被选元素添加一个或多个类
- 2.removeClass() - 从被选元素删除一个或多个类
- 3.toggleClass() - 对被选元素进行添加/删除类的切换操作
- 4.css() - 设置或返回样式属性

### 17.1 jQuery addClass()方法
使用addClass()方法可以向不同的元素添加class属性
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>jQuery教程</title>
    <script src="./js/jquery-3.2.1.min.js"></script>
    <style type="text/css">
        .important{
            font-weight: bold;
            font-size: xx-large;
        }
        .blue{
            color: blue;
        }
    </style>
</head>
<body>
    <div class="myDiv">
        <span>i am i</span>
    </div>
    <p> you are you</p>
    <button>为元素添加class</button>
    <script>
        $(document).ready(function () {
            $("button").click(function () {
                $(".myDiv,p").addClass("blue");
                $(".myDiv").addClass("important");
            });
        });
    </script>
</body>
```

### 17.2 jQuery removeClass()方法
removeClass()方法可以在元素中删除指定的class属性
##### 代码:
```html
$("#myButton2").click(function () {
	$(".myDiv,p").removeClass("blue");
	$(".myDiv").removeClass("important");
});
```

### 17.3 jQuery toggleClass()方法
toggleClass()方法综合了addClass()方法和removeClass()方法。对被选元素进行添加/删除类的切换操作。

## 18. jQuery css()方法
css()方法设置或返回被选元素的一个或多个样式属性

### 18.1 设置多个CSS属性
使用css()方法设置多个CSS属性，具体代码如下:
##### 代码:
```html
$("p").css({"background-color":"red","font-size":"200%"});
```

## 19. jQuery 尺寸
通过jQuery，很容易处理元素和浏览器窗口的尺寸,具体方法如下:

- 1.width() - Element元素宽度
- 2.height() - Element元素高度
- 3.innerWidth() - 对应的width()+padding
- 4.innerHeight() - 对应的height()+padding
- 5.outerWidth() - 对应的innerWidth()+Border
- 6.outerHeight() - 对应的innerHeight()+Border
- 7.outerWidth(true) - 对应的outerWidth()+Margin
- 8.outerHeight(true) - 对应的outerHeight()+Margin

### 19.1 jQuery尺寸
具体可以看下图，整个页面尺寸布局:
![](http://www.runoob.com/images/img_jquerydim.gif)

# 四、jQuery 遍历

















































