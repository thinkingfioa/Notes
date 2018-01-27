# CSS3教程
```
@author 鲁伟林
一直开发后端，现在开始全栈培养自己。CSS3具有非常多的新特性，已经成为学习前端必须掌握的技术。
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
background-size属性可以定义背景图片的大小。如：bcacground-size: 80px 60px
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

### 4.3 CSS3的background-origin属性
background-origin规定背景图片的定位区域。background-origin属性进一步将背景图片区域划分成三个区域:border-box、padding-box和content-box。如下图所示:

![](http://www.runoob.com/images/background-origin.gif)

##### 代码:
```html
background-origin:content-box
```

### 4.4 CSS3的background-clip属性
background-clip属性规定背景绘制区域。CSS3提供了background-clip属性实现从指定位置开始绘制背景。也是对应三个区域:border-box、padding-box和content-box;

##### 代码:
```html
.class{	
	border: 10px dotted black;
	padding: 25px;
	background: yellow;
	background-clip: content-box;
}
```

## 5. CSS3 渐变
CSS3定义了两种类型的渐变:

- 1.线形渐变 - 向下／向上／向左／向右／对角方向
- 2.径向渐变 - 由它们的中心定义

### 5.1 CSS3 线形渐变
为了创建一个线形渐变，必须至少定义两种颜色节点。基本语法: background: linear-gradient(direction, color-step1, color-step2, ...)

#### 5.1.1 线形渐变 - 从上到下(默认)
关键代码：background: linear-gradient(red, blue);
##### 代码:
```html
<head>
    <meta charset="UTF-8">
    <title>CSS3教程</title>
    <style type="text/css">
        .top-bottom{
            height: 200px;
            background: linear-gradient(red, blue);
        }
    </style>
</head>
<body>
    <div class="top-bottom"></div>
</body>
```

#### 5.1.2 线形渐变 - 从左到右
关键代码：background: linear-gradient(to right, red, blue);

#### 5.1.3 线形渐变 - 从左上到右下
关键代码：background: linear-gradient(to bottom right, red, blue);

#### 5.1.4 线形渐变 - 自定义角度
渐变方向上采取自定义角度，将会更加灵活，如下图:

![](http://www.runoob.com/wp-content/uploads/2014/07/7B0CC41A-86DC-4E1B-8A69-A410E6764B91.jpg)

##### 代码:
```html
.class{
	background: linear-gradient(90deg, red, blue);
}
```

#### 5.1.5 使用多个颜色点
语法：background: linear-gradient(direction, color-step1, color-step2, ...)。允许定义多个颜色，只需要在后面添加即可。如下代码定义3种渐变颜色
##### 代码:
```html
background: linear-gradient(90deg, red, green, blue);
```

#### 5.1.6 使用透明度
使用rgba函数定义颜色节点，可以实现透明度。rgab(255, 0, 0 , 0.5)函数的最后一个参数，是0到1的值。0表示完全透明，1表示完全不透明。
##### 代码:
```html
background: linear-gradient(to right, rgba(255, 0, 0, 0), rgba(255, 0, 0, 1));
```

#### 5.1.7 重复的线性渐变(repeating-linear-gradient())
如： background: repeating-linear-gradient(red, yellow 10%, green 20%);

### 5.2 CSS3 径向渐变
径向渐变由它的中心定义，可以定义渐变的中心、形状(圆形和椭圆形)、大小。基本语法：background: radial-gradient(center, shape size, start-color, ..., last-color);

#### 5.2.1 径向渐变 - 颜色节点均匀分布(默认情况下)
关键代码：background: radial-gradient(red, green, blue);
##### 代码:
```html
.radial-Circle{
	height:200px;
	width: 300px;
	background: radial-gradient(red, green, blue);
}
```

#### 5.2.2 径向渐变 - 颜色不均匀分布
关键代码：background: radial-gradient(red 5%, green 15%, blue 60%);

#### 5.2.3 设置形状
shape参数定义了形状，可以是值circle或eclipse。关键代码：background: radial-gradient(circle, red, yellow, green);

#### 5.2.4 重复的径向渐变(repeating-radial-gradient())
关键代码：background: repeating-radial-gradient(red, yellow 10%, green 15%);

## 6. CSS3 文本效果
CSS3中包含了几个新的文本特征，新的文本属性如下:

- 1.text-shadow
- 2.box-shadow
- 3.text-overflow
- 4.word-wrap
- 5.word-break

### 6.1 CSS3 的文本阴影(text-shadow)
使用text-shadow属性适用于文本阴影，如: text-shadow: 5px 5px 5px #ff0000;
##### 代码:
```html
.textShadow {
	text-shadow: 5px 5px 5px #ff0000;
	font-size: 30px;
}
```

### 6.2 CSS3 的盒子阴影(box-shadow)
box-shadow属性用来定义盒子属性的阴影，关键代码: box-shadow: 10px 10px 10px #7d7d7d;
##### 代码:
```
.boxShadow {
	width: 300px;
	height: 100px;
	background-color: red;
	box-shadow: 10px 10px 10px #7d7d7d;
	text-align: center;
	padding: 4px;
}
```

### 6.3 使用::before和::after两个伪元素中添加阴影效果
伪元素::before和::after来指定某个元素前、后的阴影定义
##### 代码：
```html
#boxshadow::after {
    content: '';
    position: absolute;
    z-index: -1; /* hide shadow behind image */
    box-shadow: 0 15px 20px rgba(0, 0, 0, 0.3); 
    width: 70%; 
    left: 15%; /* one half of the remaining 30% */
    height: 100px;
    bottom: 0;
}
```

### 6.4 CSS3 Text Overflow属性
使用text-overflow属性显示溢出内容

- 1.text-overflow: ellipsis - 隐藏溢出的文本
- 2.text-overflow: clip - 剪辑

##### 代码:
```html
.textOverflow {
	border: 1px solid #000000;
	width: 100px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}
```

### 6.5 CSS3的换行(word-wrap)
使用属性word-wrap来控制文本的换行，意味着自动换行允许强制文本换行
##### 代码:
```html
.textWordWrap {
	border: 1px solid #000000;
	width: 100px;
	word-wrap: break-word;
}
```

### 6.6 CSS3 单词拆分换行(word-break)
单词拆分换行指定换行规则

- 1.word-break: keep-all - 单词不换行，如果行末尾放不下，放于下段首位置
- 2.word-break: break-all - 单词直接换行，有的时候出现一个单词位于两段中

## 7. CSS3 字体
CSS3提供字体自动下载，意味着可以使用任何字体，无需限定为用户计算机已经安装的字体

### 7.1 CSS3 定义字体(@font-face)
使用@font-face定义一个字体，然后再在文本中引用，基本语法格式，参考下列的代码：
##### 代码:
```html
<style type="text/css">
@font-face
{
    font-family: myFirstFont;
    src: url(sansation_light.woff);
}
 
div
{
    font-family:myFirstFont;
}
</style>
```

## 8. CSS3 2D转换
CSS3 转换可以对元素进行移动、缩放、转动、拉长或拉伸。通俗的说，就是改变某个元素的形状、大小和位置

### 8.1 2D转换
2D变换方法:

- 1.translate() - 从当前元素位置移动
- 2.rotate() - 元素顺时针旋转
- 3.scale() - 元素增加或减少的大小
- 4.skew() - 元素的倾斜
- 5.matrix() - 将2D变换方法合并成一个
- 6.transform-Origin - 允许更改转换元素的位置

### 8.2 translate() 方法
translate()方法，根据元素原来的位置，左(X轴)和顶部(Y轴)位置给定的参数进行移动
#####  代码:
```html
div {
	border: 2px solid black;
	background-color: red;
	width:200px;
	height: 100px;
	margin-left: 100px;
	margin-top: 100px;
}
#div2 {
	transform: translate(50px, 100px);
}
``` 

### 8.3 rotate() 方法
rotate()方法，给一个度数顺时针旋转元素
##### 代码：
```html
#div2 {
	transform: translate(50px, 100px);
	transform: rotate(90deg);
}
```

### 8.4 scale() 方法
scale()方法用于放大元素的大小。如:transform: scale(2,4)转变宽度为原来的2倍，高度为3倍

### 8.5 skew() 方法
skew() 方法用于倾斜元素，语法：transform: skew(angle1, angle2)。第一个参数angle1表示X轴倾斜，第二个参数angle2表示Y轴的倾斜.
##### 代码:
```html
transform: skew(30deg, 20deg);
```

### 8.6 matrix() 方法
matrix()方法用于汇总上面多个属性，共有6个参数，包含旋转、缩放、平移、倾斜。6个参数的意义不知道，较复杂，待更新

### 8.7 transform-origin 定义起点
transform-origin设置旋转元素的基点位置，允许更改转化元素位置，比如旋转，可以自定义旋转的中心。比如案例为：transform-origin: 20% 20%;

## 9. CSS3 3D转换

### 9.1 rotateX() 方法
rotateX()方法，围绕其在一个给定度数X轴旋转的元素，如：transform: rotateX(120deg);

### 9.2 rotateY() 方法
rotateY()方法，围绕其在一个给定度数Y轴旋转的元素，如：transform: rotateY(120deg);





























