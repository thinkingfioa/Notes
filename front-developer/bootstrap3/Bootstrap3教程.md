# 一、Bootstrap3教程
```
@author 鲁伟林
Bootstrap3是目前最受欢迎的前端框架，非常重要。
参考网址是：http://www.runoob.com/bootstrap/bootstrap-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/bootstrap3/
```
---



## 1. Bootstrap简介
Bootstrap是一个快速开发Web应用程序和网站的前端框架。Bootstrap的学习需要先初步了解Html、Css、Javascript基础知识。

### 1.1 Bootstrap 包含的内容
- 1.基本结构：Bootstrap提供了一个带有网格系统、链接样式、背景的基本结构
- 2.CSS：Bootstrap提供多于基本的CSS的常用组件
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
    <script src="./bootstrap/js/bootstrap.min.js"></script>
    <script src="./jquery/jquery-3.2.1.min.js"></script>
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






























