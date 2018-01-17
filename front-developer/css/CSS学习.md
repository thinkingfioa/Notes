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
background-image属性描述了元素的背景图像





















