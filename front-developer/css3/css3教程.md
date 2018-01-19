# CSS3教程
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。CSS3具有非常多的新特性，已经成为学习前端必须掌握的技术
学习CSS3的网址是：http://www.runoob.com/css/cs3d-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/css3
```
---

## 1. CSS3简介
CSS3被拆分为"模块"，一些最重要的CSS3模块如下:

- 1.选择器
- 2.盒模型
- 3.背景和边框
- 4.文字特效
- 5.2D/3D转换
- 6.动画
- 7.多列布局
- 8.用户界面

## 2. CSS3 边框
用CSS3可以创建圆角边框、添加阴影框、并作为边界的形象，具体边框属性如下:

- 1.border-radius - 圆角
- 2.box-shadow - 用来添加阴影
- 3.border-image - 边界图片

### 2.1 CSS3 圆角(border-radius)
在CSS3中，使用border-radius属性用于创建圆角
##### 代码:
```html
div{
	border: 2px solid #b5b5b5;
	border-radius: 5px;
	width: 300px;
	text-align: center;
	background-color: lightgrey;
	padding: 8px 16px;
}
```

### 2.2 CSS3 盒阴影(box-shadow)
box-shadow属性用来定义盒阴影。语法:box-shadow: x y z red。其中x、y、z代表3个方向偏移量
##### 代码:
```html
div{
	border: 2px solid #b5b5b5;
	border-radius: 5px;
	width: 300px;
	text-align: center;
	background-color: lightgrey;
	padding: 8px 16px;
	box-shadow: 5px 5px 5px #949494;
}
```

### 2.3 CSS3 边界图片(border-image)
使用border-image属性，可以使用图像创建一个边框，如：border-image:url(border.png) 30 30 round;。我也没搞清楚30 30是什么意思，等待更新?

## 3. CSS3 圆角(border-radius)
使用属性border-radius，可以给很多元素添加圆角。如：背景、边框和图背景

### 3.1 border-radius 指定每个圆角
border-radius后可以跟多个数值。和CSS中简写属性一样，请顺时针读取

- 1.border-radius:15px 50px 30px 5px - 左上角15px、右上角50px、右下角30px、左下角5px
- 2.border-radius:15px 30px 5px - 左上角15px、右上角30px、右下角5px、左下角30px
- 3.border-radius:15px 30px - 左上角15px、右上角30px、右下角15px、左下角30px
- 4.border-radius:15px - 四个角都是15px

### 3.2 绘制椭圆
当border-radius:50%，则定义个椭圆形状

## 4. CSS3 背景
CSS3中添加了几个新的背景属性

- 1.background-image
- 2.background-size
- 3.background-origin
- 4.background-clip

### 4.1 CSS3 background-image属性
CSS3中可以使用background-image属性添加多张背景图片。多个背景图片使用逗号","分隔
##### 代码:
```html
background: url(pic1.gif) top left repeat, url(pic2.gif) right bottom no-repeat;
```

### 4.2 CSS3 background-size属性
background-size属性可以定义背景图片的大小
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS3教程</title>
    <style type="text/css">
        .myBackgroundPic{
            background: url("images/background.gif") no-repeat;
            background-size: 80px 60px;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="myBackgroundPic">
        <span>背景图片</span>
        <div class="originalPic">
            <span>原始图片:</span>
            <img src="images/background.gif">
        </div>
    </div>
</body>
```


























