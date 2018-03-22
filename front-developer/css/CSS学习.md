# CSS学习
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。
学习CSS的网址是：http://www.runoob.com/css/css-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/css
```
---

## 1. CSS 简介
### 1.1 什么是CSS?
- 1.CSS指层叠样式表(Cascading Style Sheets)
- 2.样式定义**如何显示**HTML元素
- 3.样式通常存储在样式表中
- 4.外部样式表可以极大提高工作效率
- 5.外部样式表通常存储在CSS文件中

## 2. CSS 语法
### 2.1 CSS实例
CSS规则由两个主要的部分组成：选择器 + (一条／多条)声明
![如下图](http://www.runoob.com/images/selector.gif)

### 2.2 CSS注释
CSS注释以"/\*"开始，以"\*/"结束

### 2.3 CSS Id和Class选择器
设置CSS样式，需要在元素中设置"id"和"class"选择器

- 1."id"选择器命名方式: #id
- 2."class"选择器命名方法: .className。如果定义多个class属性需要加空格，如: class="name1 name2"，name1和name2都可以作为元素的Class选择器

##### 代码
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        #p1{
            text-align: center;
            color:red;
        }
        .pClassName{
            text-align: center;
            color:green;
        }
    </style>
</head>
<body>
    <p id="p1">使用id选择器: Hello World</p>
    <p class="pClassName">使用class选择器: Hello PPP</p>
</body>
```

##### 提醒:
容易混淆的.class1.class2与.class1 .class2的区别

- 1.第一个中间没有空格，匹配的是同时拥有class1和class2的元素
- 2.第二个中间有空格，匹配的是父节点是class1类，子节点是class2类的元素


## 3. CSS创建
插入样式表的方法有三种:

- 1.外部样式表
- 2.内部样式表
- 3.内联样式

### 3.1 外部样式表
外部样式表将样式定义写到一个.css扩展名的文件。再引入到具体的html文件中。
##### 代码：
```html
<head>
	<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

### 3.2 内部样式表
内部样式表是使用标签\<style>，定义在\<head>元素中
##### 代码:
```html
<head>
    <style type="text/css">
        #p1{
            text-align: center;
            color:red;
        }
        .pClassName{
            text-align: center;
            color:green;
        }
    </style>
</head>
```

### 3.3 内联样式
使用(style)属性，定义元素的样式，请慎用这种方法
##### 代码:
```html
<p style="color:red;text-align:center;">iami</p>
```

### 3.4多重样式优先级
- 1.可能某个选择器在多个地方被定义样式，需要了解样式优先级。
- 2.(内联样式)>内部样式>外部样式>浏览器默认样式

## 4. CSS Backgrounds(背景)
CSS背景属性用于定义HTML元素的背景。CSS属性定义背景效果：

- 1.background-color
- 2.background-image
- 3.background-repeat
- 4.background-attachment
- 5.background-position

### 4.1 background-color 背景颜色
background-color属性定义元素的背景颜色，如: body{background-color:#ffffff}

### 4.2 background-image 背景图像
background-image属性描述了元素的背景图像,默认情况下，背景图像进行平铺重复显示
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body {
            background-image:url("./images/background.jpg");
            background-color:#cccccc;
        }
    </style>
</head>
<body>
    <h1>Hello World</h1>
</body>
```

### 4.3 背景图像 - 水平或垂直平铺(background-repeat)
默认情况下background-image属性会在页面的水平或垂直方向平铺。如下代码，只在水平方向上平铺(repeat-x)

- 1.repeat-x 只在水平方向上重复
- 2.repeat-y 只在垂直方向上重复
- 3.no-repeat 不重复

##### 代码:
```html
body {
	background-image.url("./images/background.jpg");
	background-repeat:repeat-x;
}
```

### 4.4 背景图像 - 设置背景图片的位置(background-position)
background-position可以指定背景图片显示位置
##### 代码:
```html
 body {
 	background-image:url("./images/background.jpg");
	background-repeat: repeat-y;
	background-position: top right;
}
```

### 4.5 背景 - 简写属性
上列介绍的多个属性，可以进行简写。浓缩成一句
##### 代码:
```html
body { backgroud:#ffffff url("./images/background.jpg") no-repeat right top}
```

## 5. CSS Text(文本)

### 5.1 文本颜色(color)
颜色属性被用来设置文字的颜色。提醒: 根据W3C标准，如果定义了颜色属性，请必须定义背景色属性
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        h1{
            color:red;
        }
        p#hello{
            color:#00ffff;
        }
        p.world{
            color:rgb(0,0,255);
        }
    </style>
</head>
<body>
    <h1>一级标题</h1>
    <p id="hello">Hello</p>
    <p class="world">World</p>
</body>
```

### 5.2 文本的对齐方式（text-align)
text-align属性用于定义文本对齐方式:

- 1.text-align:center - 居中对齐
- 2.text-align:right - 右对齐
- 3.text-align:justify - 两端对齐
- 4.text-align:left - 左对齐

### 5.3 文本修饰(text-decoration)
text-decoration属性主要用来删除链接的下划线。该属性主要用来设置或删除文本的装饰

- 1.text-decoration:none - 去除下划线
- 2.text-decoration:underline - 添加下划线

### 5.4 文本转换(text-transform)
文本转换主要用于将字句变成**大写**、**小写**和**首字母大写**

- 1.text-transform:uppercase - 变大写
- 2.text-transform:lowercase - 变小写
- 3.text-transform:capitalize - 首字母大写

### 5.5 文本缩进(text-indent)
文本缩进属性是用来指定文本第一行的缩进。如: text-indent:50px

### 5.6 添加文本阴影(text-shadow)
##### 代码:
```html
#shadow{
	text-shadow: 2px 2px #ff0000;
	font-size: 30px;
}
```

## 6. CSS字体
CSS字体属性定义字体、加粗、大小和文字样式

### 6.1 字体系列(font-family)
font-family属性设置文本字体。可以设置多种字体，防止浏览器出现不支持某种字体。[常用字体](http://www.runoob.com/cssref/css-websafe-fonts.html)
##### 代码:
```html
p{font-famili:"Times New Roma", Times, Arial}
```

### 6.2 字体样式(font-style)
- 1.font-style:normal - 正常显示文本
- 2.font-style:italic - 斜体

### 6.3 字体大小(font-size)
字体默认大小为16px=1em。可以使用font-size属性定义文字大小

### 6.4 使用百分比和em组合
为了适应所有浏览器，设置\<body>元素的默认字体大小的是百分比
##### 代码:
```html
body{ font-size:100%}
h1{font-size:2.5em}
```

### 6.5 字体加粗(font-weight)
font-weight属性用来设置字体粗细，如:

- 1.font-weight:normal - 正常
- 2.font-weight:lighter - 细体
- 3.font-weight:bold - 粗体

### 6.6 字体简写(font)
使用属性font，可以简写所有的字体属性，如:p{font:italic bold 12px/30px Georgia,serif;}

## 7. CSS 链接(link)
链接的样式，可以定义多种不同样式，
### 7.1 四个链接状态
四个链接状态如下，但是我个人觉得(解释有点问题)：

- 1.a:link - 正常，未访问的链接
- 2.a:visited - 用户已访问过的链接
- 3.a:hover - 当用户鼠标放在链接上
- 4.a:active - 链接被点击的那一刻

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        a:link {color:#000000;}      /* 未访问链接*/
        a:visited {color:#00FF00;}  /* 已访问链接 */
        a:hover {color:#FF00FF;}  /* 鼠标移动到链接上 */
        a:active {color:#0000FF;}  /* 鼠标点击时 */
        
    </style>
</head>
<body>
    <a id="blog" href="http://blog.csdn.net/thinking_fioa" target="_blank">thinking_fioa的博客地址</a>
</body>
```

### 7.2 文本修饰(text-decoration)
##### 代码:
```html
a:link {text-decoration:none;}
a:visited {text-decoration:none;}
a:hover {text-decoration:underline;}
a:active {text-decoration:underline;}
```

### 7.3 背景颜色(background-color)
背景颜色属性指定链接背景色
##### 代码:
```html
a:link {background-color:#B2FF99;}
a:visited {background-color:#FFFF85;}
a:hover {background-color:#FF704D;}
a:active {background-color:#FF704D;}
```

## 8. CSS 列表样式(ul)
使用CSS可以进一步定义列表样式，CSS列表属性作用如下:

- 1.设置不同的列表项标记为有序列表
- 2.设置不同的列表项标记为无序列表
- 3.设置列表项标记为图像

### 8.1 不同的列表项标记(list-style-type)
list-style-type属性指定列表项标记类型

- 1.list-style-type:circle - 空心圆
- 2.list-style-type:square - 实心圆
- 3.list-style-type:upper-romam - 大写罗马字符(I、II等)
- 4.list-style-type:lower-alpha - 小写字母(a、b等）
- 5.list-style-type:none - 无

### 8.2 图像作为列表项标记(list-style-image: url('some.jpg'))
列表项可以使用图片进行标记，使用list-style-image属性指定。注意：有些浏览器对于list-style-image属性显示可能存在一点差别
##### 代码:
```html
ul{
	list-style-image: url("some_image.jpg");
}
```

### 8.3 列表-简写属性
通过list-style属性，将所有列表属性汇总，简写成一句话
##### 代码:
```html
ul{
	list-style: square url("some_image.jpg");
}
```

## 9. CSS Table(表格)

### 9.1 表格边框(border)
使用属性来定义表格边框
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        table, th,td{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th>FirstName</th>
            <th>LastName</th>
        </tr>
        <tr>
            <td>thinking</td>
            <td>fioa</td>
        </tr>
        <tr>
            <td>ppp</td>
            <td>cuter</td>
        </tr>
    </table>
</body>
```

### 9.2 折叠边框(border-collapse)
使用border属性，可能每个元素都会有边框，会存在边框重叠。使用border-collapse折叠边框
##### 代码:
```html
<style type="text/css">
	table{
		border-collapse: collapse;
	}
	table, th,td{
		border: 1px solid black;
	}
</style>
```

### 9.3 表格高度(width)
使用width属性,如: th{ width:100%;}

### 9.4 表格文字对齐(text-align)
使用text-align属性设置水平对齐,如: td{text-align:left;}

### 9.5 表格填充(padding)
在表的内容与控制空格之间边框的间隙。如: td{padding: 5px;}

### 9.6 设置表格标题的位置(caption-side}
##### 代码:
```html
caption{
	caption-side: bottom;
}
```

## 10. CSS盒子模型(Box Model)
所有的HTML元素都可以看作盒子，在CSS中,"Box Model"用来设计和布局元素位置使用，主要包括:
外边距、边框、内边距、内容。具体说明如下:

- 1.Margin(外边距) - 清除边框外的区域，外边是透明的
- 2.Border(边框) - 围绕在内边距的边框
- 3.Padding(内边距) - 清除内容周围的区域，内边距是透明的
- 4.Content(内容) - 盒子的具体内容，包括文本和图像等

具体参见下图:

![Mox Model](http://www.runoob.com/images/box-model.gif)

### 10.1 元素的宽度和高度(width、height)
特别提醒：当你指定一个CSS元素的宽度和高度时，你只是在设置内容区域(Content)的宽度和高度。然而整个元素的大小，还包括Margin、Border和Padding。如下代码，总长度是:300+25\*2+25\*2+25\*2 = 450

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        div{
            display: block;
            width:300px;
            border:25px solid green;
            background-color: lightgrey;
            padding:25px;
            margin:25px;
        }
    </style>
</head>
<body>
    <div>
        这里是内容区域
    </div>
</body>
```

## 11. CSS Border(边框)
CSS边框属性允许你指定一个元素边框的样式和颜色

### 11.1 边框样式(border-style)
border-style属性用来定义边框的样式。如下:

- 1.none:默认无边框
- 2.dashed:定义一个虚线边框
- 3.solid:定义实线边框
- 4.double:定义两个边框

### 11.2 边框宽度(border-width)
通过border-width属性定义边框指定宽度，如: p{border-width:2px;}

### 11.3 边框颜色(border-color)
border-color属性定义边框的颜色，如: p { border-color:red;}

### 11.4 边框-简写属性(border)
使用border属性来简写边框，如：border{2px solid red;}

## 12. CSS 轮廓(outline)属性
轮廓(outline)位于border和margin之间的元素属性，可其中突出元素的作用。目前先暂且不补充，后续再更新

## 13. CSS Margin(外边距)
CSS Margin(外边距)属性定义元素周围的空间。margin没有背景颜色，是完全透明的

### 13.1 Margin - 单边外边距属性
在CSS中，可以指定不同的侧面不同的边距

- 1.margin-top - 顶部
- 2.margin-bottom - 底部
- 3.margin-left - 左边
- 4.margin-right - 右边

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        .margin{
            margin-top:50px;
            margin-left:50px;
            margin-right:50px;
            margin-bottom:50px;
        }
    </style>
</head>
<body>
    <p class="margin">这是一个指定Margin属性的P元素</p>
</body>
```

### 13.2 Margin - 简写属性
为了缩短代码，可以使用margin来缩写属性，全写的话是顺时针

- 1.margin:25px 50px 75px 100px - 上边距25px,右边距50px,下边距75px，左边距100px
- 2.margin:25px 50px 75px - 上边距25px,左右边距50px,下边距75px
- 3.margin:25px 50px - 上下边距25px,左右边距50px

## 14. CSS Padding(填充)
CSS Padding(填充)属性定义元素边框在元素内容之间的空间

### 14.1 填充 - 单边内边距属性
在CSS中，可以指定不同的侧面不同的填充:

- 1.padding-top - 顶部
- 2.padding-bottom - 底部
- 3.padding-left - 左边
- 4.padding-right - 右边

### 14.2 填充简写
为了缩短代码，可以使用padding来缩写属性。具体位置与margin一模一样。全写的话是顺时针

- 1.padding:25px 50px 75px 100px - 上填充25px,右填充50px,下填充75px，左填充100px
- 2.padding:25px 50px 75px - 上填充25px,左右填充50px,下填充75px
- 3.padding:25px 50px - 上下填充25px,左右填充50px

## 15. CSS 分组和嵌套选择器
在CSS中可能会存在非常多的相同的样式，使用分组和嵌套来减少代码，方便维护

### 15.1 分组
将多个元素用逗号(,)分割，定义相同的样式
##### 代码:
```html
h1,h2,p{
	color:red;
}
```

### 15.2 嵌套选择器
当选择器内部样式需要定制化时，使用嵌套选择器。如下代码表示：className类下了嵌套元素p(子元素)
##### 代码:
```html
.className p{
	color:white;
}
```

## 16. CSS 尺寸(Dimension)
利用尺寸属性可以控制元素的高度和宽度。同样，也可以增加行间距

|属性|描述|
|:---|:---|
|height|设置元素的高度|
|line-height|设置行高|
|max-height|设置元素的最大高度|
|max-width|设置元素的最大宽度|
|min-height|设置元素的最小高度|
|min-width|设置元素的最小宽度|
|width|设置元素的宽度|

### 16.1 设置行高(line-height)
如果希望元素在对应的区域内居中，需要使用行高
##### 代码:
```html
p{
	text-align:center;
	line-height:100px;
}
```

## 17. CSS Display(显示)与Visibility(可见性)
display元素设置一个元素应如何显示，visibility属性指定一个元素应可见还是隐藏

### 17.1 隐藏元素 - display:none或visibility:hidden
- 1.display:none - 隐藏一个元素，且隐藏的元素不会占用任何空间
- 2.visibility:hidden - 隐藏一个元素，但是隐藏的元素占用的空间仍然保留，会影响布局。

### 17.2 Display - 块和内联元素
- 1.display:block - 块元素显示。会在元素前后加上换行符
- 2.display:inline - 内联元素显示。不换行
- 3.display:inline-block - 显示内联块元素，表现为同行显示并可修改宽高内外边距等属性。通常将\<ul>加上display:inline-block

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        .inline *{
            display: inline;
        }
        .block {
            display: block;
        }
    </style>
</head>
<body>
    <div class="inline">
        <p>内联元素:</p>
        <p>thinking_fioa</p>
    </div>
    <div class="block">
        <p>块元素:</p>
        <p>ppp</p>
    </div>
</body>
```

## 18. CSS Positioning(定位)
position属性指定了元素的定位类型。position属性的四个值。static和relative在文档流中，与fixed和absolute相反。

- 1.static  
- 2.relative
- 3.fixed
- 4.absolute

### 18.1 static 定位
- 1.static是position的缺省值，一般不设置position属性时，默认是static。
- 2.静态定位元素(static)不会受到top，bottom，left，right影响

### 18.2 relative
- 1.相对本身位置的偏移(static定位下的元素位置为本身位置)。
- 2.受到top、bottom、left、right影响
- 3.且不会影响后面其他元素的位置。
- 4.原本空间不会改变(static和relative在文档流中，与fixed和absolute相反)

##### 代码:
```html
.relative_pos{
	position: relative;
	left:-20px;
}
```


### 18.3 fixed 定位
fixed是特殊的absolute，即fixed总是以浏览器的可视窗口(屏幕内网页窗口)进行定位。不占据空间
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        .fixed_pos{
            position: fixed;
            top:50px;
            right:10px;
        }
    </style>
</head>
<body>
    <p class="fixed_pos">someone like you</p>
</body>
```

### 18.4 absolute 定位
当一个元素A设置了position:absolute后，分为两种情况:

- 1.当元素A的父对象设置了position属性，且position的属性值为absolute或relative或fixed，也就是说不是默认的，则元素A按照父对象来定位。如果父对象设置了margin、border、padding等属性，则元素A将会从padding开始的地方进行定位
- 2.如果元素A没有一个position属性的父对象，则以body为定位对象

##### 代码:
```html
h2{	
	postion:absolute;
	left:100px;
	top:50px;
}
```

### 18.5 重叠的元素(z-index)
使用元素定位属性:position会导致元素重叠，可以使用属性:z-index，来规定谁置底
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        .fixed_pos{
            position: fixed;
            top:70px;
            left:40px;
        }
        .pic{
            position: fixed;
            top:50px;
            left:10px;
            z-index:-1;
        }
    </style>
</head>
<body>
    <p class="fixed_pos">someone like you</p>
    <img class="pic" src="https://avatar.csdn.net/F/7/8/1_thinking_fioa.jpg">
<\body>
```

## 19. CSS Float(浮动)
Float(浮动)往往用于图像，会使元素向左或向右移动。

### 19.1 元素怎样浮动
- 1.元素的水平方向浮动，意味着元素只能左右移动而不能上下移动。
- 2.一个浮动元素会尽量向左或向右移动，直到它的外边碰到包含边框或另一个边框

### 19.2 彼此相邻的浮动元素
将多个浮动元素放在一起，如果有空间的话，它们会彼此相邻
##### 代码:
```html
.thumbnail{
	float:left;
	width:110px;
	height:90px;
	margin:5px;
}
```

### 19.3 清除浮动 - 使用clear
- 1.元素浮动之后，周围的元素会重新排列，为了避免这种情况，使用 clear 属性
- 2.clear 属性指定元素两侧不能出现浮动元素
- 3.clear可以用来截断元素浮动，因为浮动元素
- 4.基本语法: p{clear:both;}

##### 代码:
```html
<style>
.thumbnail 
{
	float:left;
	width:110px;
	height:90px;
	margin:5px;
}
.text_line
{
	clear:both;
	margin-bottom:2px;
}
</style>
</head>

<body>
<h3>图片库</h3>
<p>试着调整窗口,看看当图片没有足够的空间会发生什么。.</p>
<img class="thumbnail" src="/images/1.jpg" width="107" height="90">
<img class="thumbnail" src="/images/2.jpg" width="107" height="80">
<img class="thumbnail" src="/images/3.jpg" width="116" height="90">
<img class="thumbnail" src="/images/4.jpg" width="120" height="90">
<h3 class="text_line">第二行</h3>
<img class="thumbnail" src="/images/1.jpg" width="107" height="90">
<img class="thumbnail" src="/images/2.jpg" width="107" height="80">
<img class="thumbnail" src="/images/3.jpg" width="116" height="90">
<img class="thumbnail" src="/images/4.jpg" width="120" height="90">
</body>
```

## 20. CSS 对齐
水平 & 垂直居中对齐

### 20.1 元素居中对齐(margin:auto)
使用margin:auto来水平居中对齐一个元素，请必须指定width属性
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        div{
            margin:auto;
            border: 5px solid green;
            width:50%;
            padding:10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div>thinking_fioa</div>
</body>
```

### 20.2 文本居中对齐
文本居中对齐使用text-algin属性，如:text-align:center;

### 20.3 图片居中对齐
要让图片居中对齐，可以使用margin:auto，同时并使用块元素显示,display:block
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        .myPic{
            margin: auto;
            display: block;
        }
    </style>
</head>
<body>
    <img class="myPic" src="https://avatar.csdn.net/F/7/8/1_thinking_fioa.jpg">
</body>
```

### 20.4 左右对齐-使用定位方式(position)
使用position:absolute属性定义元素位置
##### 代码:
```html
.right{
	position:absolute;
	right:0px;
	width:300px;
	padding:10px;
	border: 3px solid green;
}
```

### 20.5 左右对齐-使用float方式
使用float属性来对齐元素。float属性通常用于图片的对齐
##### 代码:
```html
.right{
	float:right;
	width:300px;
	padding:10px;
	border: 3px solid green;
}
```

### 20.6 垂直居中对齐 - 使用padding
CSS中有多种方式实现垂直居中对齐。一种简单的方式就是头部和底部使用padding
##### 代码:
```html
.center{
	padding: 40px 0;
	border: 3px solid lightgrey;
}
```

### 20.7 垂直居中 - 使用line-height
line-height设置行高，可用来设置垂直居中
##### 代码:
```html
.center {
    line-height: 200px;
    height: 200px;
}
```

### 20.8 垂直居中 - 使用position和transform
可以使用transform属性来设置垂直居中 
##### 代码:
```html
<style>
	.center { 
   		height: 200px;
   		position: relative;
    	border: 3px solid green; 
	}
	.center p {
    	margin: 0;
    	position: absolute;
    	top: 50%;
    	left: 50%;
    	-ms-transform: translate(-50%, -50%);
    	transform: translate(-50%, -50%);
	}
</style>
```

## 21. CSS 组合选择符
组合选择器说明两个选择器具有直接的关系，CSS3中包含了四种组合方式：

- 1.后代选择器(以空格分隔)
- 2.子元素选择器(以大于号分隔)
- 3.相邻兄弟选择器(以加号分隔)
- 4.普通兄弟选择器(以破折号分隔)

### 21.1 后代选取器(div p)
后代选取器匹配指定元素的子元素，如下代码，表示指定元素\<div>的所有子元素\<p>
##### 代码:
```html
div p{
	background-color:yellow;
}
```

### 21.2 子元素选择器(div>p)
子元素选择器，只能选择指定元素的直接子元素，跨级不行
##### 代码:
```html
div>p{
	background-color: yellow;
}
```

### 21.3 相邻兄弟选择器(div+p)
如:div+p，表示的是：和\<div>元素是兄弟元素，且和该\<div>元素同一级别的随后第一个\<p>类型元素
##### 代码:
```html
div+p{
	background-color: yellow;
}
```

### 21.4 后续兄弟选择器(div~p)
如:div～p，表示的是：和\<div>元素是兄弟元素，且和该\<div>元素同一级别的随后所有\<p>类型元素
##### 代码:
```html
div~p{
	background-color: yellow;
}
```

## 22. CSS 伪类
CSS伪类用来添加一些选择器的特殊效果。如a:link、a:visited等。

### 22.1  :first-child伪类
可以使用:first-child伪类来选择元素的第一个子元素
##### 代码:
```html
div>p:first-child{
	color:blue;
}
```

## 23. 伪元素
CSS伪元素是用来添加一些选择器的特殊效果，后续更新

## 24. 导航栏
熟练使用导航栏，对于所有网站都非常重要。[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/24.html)

### 24.1 垂直导航条实例
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        ul{
            margin:0;
            padding:0;
            width:150px;
            background-color:lightgrey;
            list-style-type: none;
        }
        li a{
            display:block;
            padding-left:16px;
            font-size:18px;
            text-decoration: none;
            color:black;
        }
        .active{
            background-color: #46cb72;
            color:white;
        }
        a:hover{
            color:white;
            background-color: #151827;
        }

    </style>
</head>
<body>
    <div>
        <span>垂直导航条</span>
    </div>
    <ul class="nav">
        <li><a class="active" href="javascript:void(0);">主页</a></li>
        <li><a href="javascript:void(0);">新闻</a></li>
        <li><a href="javascript:void(0);">联系</a></li>
        <li><a href="javascript:void(0);">关于</a></li>
    </ul>
</body>
```

### 24.2 全屏高度的固定导航条
下列代码实现的是: 左边是全屏高度的固定导航条，右边是可滚动的内容。[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/24_2.html)
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body{
            margin: 0;
        }
        ul{
            margin:0;
            padding:0;
            list-style-type: none;
            position: fixed;
            width: 20%;
            height: 100%;
            background-color: lightgrey;
            overflow: auto;
        }
        li a{
            display: block;
            font-size:18px;
            padding: 8px 16px;
            text-decoration: none;
            color: black;
        }
        li a.active{
            background: #46cb72;
            color: white;
        }
        li a:hover{
            background-color: #121520;
            color: white;
        }
        .content {
            margin-left:20%;
            padding: 1px 10px;
            position:absolute;
            width:80%;
            height:100%;
        }
    </style>
</head>
<body>
    <ul class = "nav" >
        <li><a class="active" href="javascript:void(0);">主页</a></li>
        <li><a href="javascript:void(0);">新闻</a></li>
        <li><a href="javascript:void(0);">联系</a></li>
        <li><a href="javascript:void(0);">关于</a></li>
    </ul>
    <div class="content">
        <h2>Fixed Full-height Side Nav</h2>
        <h3>Try to scroll this area, and see how the sidenav sticks to the page</h3>
        <p>someone like me</p>
        <p>i am i</p>
        <p>who are you</p>
        <p>you are you</p>
    </div>
</body>
```

### 24.3 水平导航条实例
使用float:left来实现水平导航条。[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/24_3.html)
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body{
            margin:0;
            padding:0;
        }
        ul{
            background-color: lightgrey;
            margin-left: 15px;
            margin-top: 15px;
            position: fixed;
            padding: 0;
            width:100%;
            list-style-type: none;
        }
        li a{
            display: block;
            float:left;
            padding: 8px 16px;
            text-decoration: none;
            color: black;
        }
        .active{
            background-color: #46cb72;
            color: white;
        }
        a:hover{
            background-color: #151827;
            color:white;
        }
    </style>
</head>
<body>
    <ul class="nav">
        <li><a class="active" href="javascript:void(0);">主页</a></li>
        <li><a href="javascript:void(0);">新闻</a></li>
        <li><a href="javascript:void(0);">联系</a></li>
        <li><a href="javascript:void(0);">关于</a></li>
    </ul>
</body>
```

## 25. CSS 下拉菜单
使用CSS创建一个鼠标移动上去后显示下拉菜单的效果

### 25.1 基本下拉菜单
基本下拉菜单实现功能: 鼠标放到对应的文字上，显示菜单。主要利用代码: .myDiv:hover .invisibility{display: blcok}。[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/25.html)
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body{
            margin: 0;
            padding: 0;
        }
        .myDiv {
            margin-top: 20px;
            margin-left: 20px;
        }
        .invisibility{
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            padding: 12px 16px;
        }
        .myDiv:hover .invisibility {
            display:block;
        }
    </style>
</head>
<body>
    <div class="myDiv">
        <span>Hello 隐形者</span>
        <div class="invisibility">
            <p>Who are you?</p>
            <p>Who am i?</p>
        </div>
    </div>
</body>
```

### 25.2 下拉菜单
创建下拉菜单，并允许用户选取列表中的某一项。主要代码：.menu:hover .invisibility{display: block;}。 [效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/25_2.html)
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body{
            margin: 0;
            padding: 0;
        }
        .menu {
            margin-top: 15px;
            margin-left: 20px;
            width: 150px;
        }
        .menu .button{
            background-color: #4CAF50;
            padding: 16px;
            color: white;
            font-size: 18px;
            cursor: pointer;
        }
        .menu .invisibility {
            display: none;
            background-color: #f9f9f9;
            position: fixed;
            width: 150px;
        }

        .menu:hover .invisibility{
            display: block;
        }
        a {
            display: block;
            text-decoration: none;
            color: black;
            font-size: 15px;
            padding: 8px 16px;
        }
        a:hover{
            background-color: #414141;
            color: white;
        }
    </style>
</head>
<body>
    <div class="menu">
        <button class="button">下拉菜单</button>
        <div class="invisibility">
            <a href="javascript:void(0);">教程1</a>
            <a href="javascript:void(0);">教程2</a>
            <a href="javascript:void(0);">教程3</a>
        </div>
    </div>
</body>
```

## 26. CSS 提示工具
CSS可以实现鼠标放上去，显示提示文本，等待后续更新，目前没有用到

## 27. 图片廊
使用CSS创建图片廊。[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/27.html)
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body {
            margin: 0;
            padding: 0;
        }
        .imageGallery{
            margin-top: 30px;
            margin-left: 30px;
            width: 100%;
        }
        .img {
            display:block;
            border: 1px solid lightgrey;
            float: left;
            margin: 5px;
        }
        .img:hover{
            border: 1px solid #afafaf;
            cursor: pointer;
        }
        .desc{
            padding:15px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="imageGallery">
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo1.jpg" target="_blank">
                <img src="./images/27_1.jpg" alt="图片无法加载" width="200" height="150">
            </a>
            <div class="desc">添加图片描述文本</div>
        </div>
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo2.jpg" target="_blank">
                <img src="./images/27_2.jpg" alt="图片无法加载" width="200" height="150">
            </a>
            <div class="desc">添加图片描述文本</div>
        </div>
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo3.jpg" target="_blank">
                <img src="./images/27_3.jpg" alt="图片无法加载" width="200" height="150">
            </a>
            <div class="desc">添加图片描述文本</div>
        </div>
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo4.jpg" target="_blank">
                <img src="./images/27_4.jpg" alt="图片无法加载" width="200" height="150">
            </a>
            <div class="desc">添加图片描述文本</div>
        </div>
    </div>
</body>
```

## 28. CSS图像透明/不透明
使用CSS非常容易创建透明的图像，使用属性opacity: 0.4来实现。主要代码是:img:hover{opacity:1}，[效果](http://htmlpreview.github.io/?https://github.com/thinkingfioa/Notes/blob/master/front-developer/css/examples/28.html)

##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS教程</title>
    <style type="text/css">
        body{
            margin: 0;
            padding: 0;
        }
        .pics{
            margin-top: 15px;
            margin-left:15px;
            width: 100%;
        }
        .img img{
            opacity: 0.5;
            float: left;
            border: 1px solid lightgrey;
            margin: 5px;
        }
        img:hover{
            border: 1px solid red;
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="pics">
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo1.jpg" target="_blank">
                <img src="images/27_1.jpg" width="200" height="150">
            </a>
        </div>
        <div class="img">
            <a href="http://static.runoob.com/images/demo/demo2jpg" target="_blank">
                <img src="images/27_2.jpg" width="200" height="150">
            </a>
        </div>
    </div>
</body>
```

## 29. CSS 图像拼合技术
当网页显示时，加载过多的图像，可能会拖慢网页显示速度。利用图像拼合技术，通俗的说就是，将多个图片放在一个大图片里面，再利用图像拼合技术，局部显示图片。等待后续更新

## 30. CSS实例
[CSS实例参考](http://www.runoob.com/css/css-examples.html)


























