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
- 2."class"选择器命名方法: .className

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
font-weight属性用来设置自己粗细，如:

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























