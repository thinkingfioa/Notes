# Bootstrap3插件教程
```
@author 鲁伟林
本博客主要讲述Bootstrap插件使用
参考网址是：http://www.runoob.com/bootstrap/bootstrap-tutorial.html
gitHub地址: https://github.com/thinkingfioa/Notes/tree/master/front-developer/bootstrap3-plugin/
```
---

## 1. Bootstrap 插件概览
Bootstrap自带12种jQuery插件。利用Bootstrap数据API，大部分的插件可以在不编写任何代码情况下被触发。站点应用Bootstrap插件的方式有两种：

- 1.单独引用：使用Bootstrap的个别的*.js文件，请注意插件之间的依赖关系
- 2.编译(同时)引用：使用bootstrap.js或bootstrap.min.js

### 1.1 data属性
通过data属性API能使用所有的Bootstrap插件。data属性应该成为首选方式

- 1.关闭data属性功能。具体方法:$(document).off('.data-api')

### 1.2 编程方式的API
Bootstrap插件提供了纯JavaScript方式的API。如:\$(".btn.danger").button("toggle").addClass("fat");

### 1.3 事件
Bootstrap提供两种形式的事件:

- 1.动词不定式：在事件开始时被触发。能够在事件开始前停止操作的执行。例如ex:show
- 2.过去分词形式：在动作执行完毕后被触发。例如ex:shown

## 2. Bootstrap模态框(Modal)插件
模态框(Modal)是覆盖在父窗体上的子窗体，类似于windows下的对话框。

### 2.1 用法
切换模态框(Modal)插件的隐藏内容:

- 1.通过data属性：在控制器元素(如按钮或链接)上设置属性data-toggle="modal"，同时设置data-target="#identifier"或href="#identifier"来指定要切换的特定的模态框(带有id="identifier")
- 2.通过JavaScript：通过JavaScript来调用带有id="identifier"的模态框。如:\$('#identifier').modal(options)

##### 代码:
```html
<h3>创建模态框(Model)</h3>
<button class="btn btn-primary" data-toggle="modal" data-target="#myModal">
    开始演示模态框
</button>
<div class="modal fade" id="myModal" tabindex="-1" role="dialog"
     aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                    &times
                </button>
                <h4 class="modal-title" id="myModalLabel">
                    模态框(modal)标题
                </h4>
            </div>
            <div class="modal-body">
                这里添加内容文本
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">
                    关闭
                </button>
                <button type="button" class="btn btn-primary">
                    提交更改
                </button>
            </div>
        </div>
    </div>
</div>
```

### 2.2 方法
下列有与modal()一起使用的有用方法:

- 1.modal(options) - 把内容作为模态框激活。接收一个可选的选项对象
- 2.modal('toggle') - 手动切换模态框
- 3.modal('show') - 手动打开模态框
- 4.modal('hode') - 手动隐藏模态框

### 2.3 事件
下列是模态框用到的事件。这些事件可以在函数中当钩子使用:

- 1.show.bs.modal - 调用show方法后出发
- 2.shown.bs.modal - 当模态框对用于可见时触发
- 3.hide.bs.modal - 当调用hide实例方法时触发
- 4.hidden.bs.modal - 当模态框全完对用户隐藏时触发

##### 代码:
```html
<script>
    $(function () { $('#myModal').on('hidden.bs.modal', function () {
            alert('现在的我，心情很难受!');
        }
    )});
</script>
```

## 3. Boostrap下拉菜单(dropdown)插件
Bootstrap3基础教程中讲解了下拉菜单，但没有涉及交互。接下来将具体讲解下拉菜单的交互

### 3.1 用法
切换下拉菜单(Dropdown)插件的隐藏内容:

- 1.通过data属性:向链接或按钮添加data-toggle="dropdown"来切换下拉菜单
- 2.通过JavaScript:通过JavaScript调用下拉菜单切换。方法:\$('.dropdown-toggle').dropdown()

### 3.2 方法
使用代码:\$().dropdown('toggle')来显示或隐藏下拉菜单，下列代码演示了下拉菜单(Dropdown)插件方法的用法:

##### 代码:
```html
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Apple公司</a>
        </div>
        <div id="myexample">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">iPad</a></li>
                <li><a href="#">iMac</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        iPhone
                        <b class="caret"></b>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a id="action-1" href="#">iPhon5</a></li>
                        <li><a href="#">iPhone5</a></li>
                        <li class="divider"></li>
                        <li><a href="#">iPhone6</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<script>
    $(function(){
        $('.dropdown-toggle').dropdown('toggle');
    })
</script>
```

## 4. Bootstrap滚动监听(scrollspy)插件
滚动监听插件，即自动更新导航插件，会根据滚动条的位置自动更新对应的导航目标

### 4.1 用法
向顶部导航添加滚动监听行为：

- 1.通过data属性：向想要监听的元素(通常是body)添加data-spy="scroll"
- 2.通过JavaScript：通过JavaScript调用滚动监听。先选取要监听的元素，然后调用.scrollspy()函数
- 3.class .data-offset：计算滚动位置时，距离顶部的偏移像素

##### 代码:
```html
<nav id="navbar-example" class="navbar navbar-default navbar-static" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button class="navbar-toggle" type="button" data-toggle="collapse"
                    data-target=".bs-js-navbar-scrollspy">
                <span class="sr-only">切换导航</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">教程名称</a>
        </div>
        <div class="collapse navbar-collapse bs-js-navbar-scrollspy">
            <ul class="nav navbar-nav">
                <li><a href="#ios">iOS</a></li>
                <li><a href="#svn">SVN</a></li>
                <li class="dropdown">
                   <a href="#" id="navbarDrop1" class="dropdown-toggle" data-toggle="dropdown">
                       <span>Java</span>
                       <b class="caret"></b>
                   </a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="navbarDrop1">
                        <li><a href="#jmeter" tabindex="-1">jmeter</a> </li>
                        <li><a href="#ejb" tabindex="-1">ejb</a></li>
                        <li class="divider"></li>
                        <li><a href="#spring" tabindex="-1">spring</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div data-spy="scroll" data-target="#navbar-example" data-offset="0"
     style="height:200px;overflow:auto;position: relative">
    <h4 id="ios">iOS</h4>
    <p>iOS是一个操作系统</p>
    <h4 id="svn">SVN</h4>
    <p>SVN是一个版本控制系统软件</p>
    <h4 id="jmeter">jMeter</h4>
    <p>jMeter测试软件</p>
    <h4 id="ejb">EJB</h4>
    <p>EJB部署应用程序服务器</p>
    <h4 id="spring">Spring</h4>
    <p>Spring开源Java框架</p>
</div>
```

### 4.2 方法(scrollspy('refresh')
当DOM中元素发生变更时(添加或删除)，需要调用scrollspy来更新DOM。如:.scrollspy('refresh')

##### 代码:
```html
<nav id="navbar-example" class="navbar navbar-default navbar-static" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <button class="navbar-toggle" type="button" data-toggle="collapse"
                    data-target=".bs-js-navbar-scrollspy">
                <span class="sr-only">切换导航</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">教程名称</a>
        </div>
        <div class="collapse navbar-collapse bs-js-navbar-scrollspy">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#ios">iOS</a></li>
                <li><a href="#svn">SVN</a></li>
                <li class="dropdown">
                   <a href="#" id="navbarDrop1" class="dropdown-toggle" data-toggle="dropdown">
                       <span>Java</span>
                       <b class="caret"></b>
                   </a>
                    <ul class="dropdown-menu" role="menu" aria-labelledby="navbarDrop1">
                        <li><a href="#jmeter" tabindex="-1">jmeter</a> </li>
                        <li><a href="#ejb" tabindex="-1">ejb</a></li>
                        <li class="divider"></li>
                        <li><a href="#spring" tabindex="-1">spring</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
<div data-spy="scroll" data-target="#navbar-example" data-offset="0"
     style="height:200px;overflow:auto;position: relative">
    <div class="section">
        <h4 id="ios">iOS<small><a href="#" onclick="removeSection(this);">&times;删除该部分</a></small></h4>
        <p>iOS是一个操作系统</p>
    </div>
    <div class="section">
        <h4 id="svn">SVN</h4>
        <p>SVN是一个版本控制系统软件</p>
    </div>
    <div class="section">
        <h4 id="jmeter"><small><a href="#" onclick="removeSection(this);">&times;删除该部分</a></small>jMeter</h4>
        <p>jMeter测试软件</p>
    </div>
    <div class="section">
        <h4 id="ejb">EJB</h4>
        <p>EJB部署应用程序服务器</p>
    </div>
    <div class="section">
        <h4 id="spring">Spring</h4>
        <p>Spring开源Java框架</p>
    </div>
</div>
<script>
    $(function() {
        removeSection = function(e){
            $(e).parents(".section").remove();
            $('[data-spy="scroll"]').each(function(){
               var $spy=$(this).scrollspy('refres')
            });
        }
        $('#navbar-example').scrollspy();
    });
</script>
```

### 4.3 事件
列出滚动监听中要用到的事件。可以用作钩子使用。

- 1.activate.bs.scrollspy - 当一个项目被滚动监听激活后，触发该事件

##### 代码:
```html
<script>
    $(function() {
        removeSection = function(e){
            $(e).parents(".section").remove();
            $('[data-spy="scroll"]').each(function(){
               var $spy=$(this).scrollspy('refres')
            });
        }
        $('#navbar-example').scrollspy();
        $('#navbar-example').on('activate.bs.scrollspy', function(){
            var currentItem=$(".nav li.active >a").text();
            $('#activeitem').html('目前正在查看 - '+currentItem);
        })
    });
</script>
```

### 4.4 创建水平滚动监听
##### 代码:
```html
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">WebSiteName</a>
        </div>
        <div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav">
                    <li><a href="#section1">Section 1</a></li>
                    <li><a href="#section2">Section 2</a></li>
                    <li><a href="#section3">Section 3</a></li>
                    <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Section 4 <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#section41">Section 4-1</a></li>
                            <li><a href="#section42">Section 4-2</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</nav>

<div id="section1" class="container-fluid">
    <h1>Section 1</h1>
    <p>Try to scroll this section</p>
</div>
<div id="section2" class="container-fluid">
    <h1>Section 2</h1>
    <p>Try to scroll this section</p>
</div>
<div id="section3" class="container-fluid">
    <h1>Section 3</h1>
    <p>Try to scroll this section</p>
</div>
<div id="section41" class="container-fluid">
    <h1>Section 4 Submenu 1</h1>
    <p>Try to scroll this section</p>
</div>
<div id="section42" class="container-fluid">
    <h1>Section 4 Submenu 2</h1>
    <p>Try to scroll this section</p>
</div>
```

### 4.5 创建垂直滚动监听
##### 代码:
```html
<body data-spy="scroll" data-target="#myScrollspy" data-offset="20">

<div class="container">
    <div class="row">
        <nav class="col-sm-3" id="myScrollspy">
            <div class="container-fluid">
                <div class="container-fluid">
                    <ul class="nav nav-pills nav-stacked">
                        <li class="active"><a href="#section1">Section 1</a></li>
                        <li><a href="#section2">Section 2</a></li>
                        <li><a href="#section3">Section 3</a></li>
                        <li class="dropdown">
                            <a class="dropdown-toggle" data-toggle="dropdown" href="#">Section 4 <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="#section41">Section 4-1</a></li>
                                <li><a href="#section42">Section 4-2</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="col-sm-9">
            <div id="section1">
                <h1>Section 1</h1>
                <p>Try to scroll this section</p>
            </div>
            <div id="section2">
                <h1>Section 2</h1>
                <p>Try to scroll this section</p>
            </div>
            <div id="section3">
                <h1>Section 3</h1>
                <p>Try to scroll this section/p>
            </div>
            <div id="section41">
                <h1>Section 4-1</h1>
                <p>Try to scroll this section</p>
            </div>
            <div id="section42">
                <h1>Section 4-2</h1>
                <p>Try to scroll this section/p>
            </div>
        </div>
    </div>
</div>
```

## 5. Bootstrap 标签页(Tab)插件
使用插件可以把内容放置在标签页或者胶囊式标签页甚至是下拉菜单标签页中

### 5.1 用法
通过以下两个方式启动标签页:

- 1.通过data属性：添加data-toggle="tab"或data-toggle="pill"到链接文本中
- 2.通过JavaScript：如:\$(this).tab('show');

### 5.2 淡入淡出效果(tab-pane fade)
添加.fade到每个.tab-pane中。第一个必须添加.in类

##### 代码:
```html
<ul id="myTab" class="nav nav-tabs">
    <li class="active">
        <a href="#home" data-toggle="tab">Apple公司</a>
    </li>
    <li>
        <a href="#iPad" data-toggle="tab">iPad</a>
    </li>
    <li class="dropdown">
        <a href="#" id="myTabDrop1" class="dropdown-toggle" data-toggle="dropdown">
            iPhone
            <b class="caret"></b>
        </a>
        <ul class="dropdown-menu" role="menu" aria-labelledby="myTabDrop1">
            <li><a href="#iPhone6" tabindex="-1" data-toggle="tab">iPhone6</a></li>
            <li><a href="#iPhone6s" tabindex="-1" data-toggle="tab">iPhone6s</a></li>
        </ul>
    </li>
</ul>
<div id="myTabContent" class="tab-content">
    <div class="tab-pane fade in active" id="home">
        <p>Apple公司</p>
    </div>
    <div class="tab-pane fade" id="iPad">
        <p>iPad产品</p>
    </div>
    <div class="tab-pane fade" id="iPhone6">
        <p>iPhone6手机</p>
    </div>
    <div class="tab-pane fade" id="iPhone6s">
        <p>iPhone6s手机</p>
    </div>
</div>
```

### 5.3 方法
.\$().tab方法可以激活标签页元素和内容容器

##### 代码:
```html
<script>
    $(function () {
        $('#myTab li:eq(1) a').tab('show');
    })
</script>
```

### 5.4 事件
标签页提供多个事件，如下：

- 1.show.bs.tab - 标签页被显示前触发。使用event.target和event.relatedTarget来定位到激活的标签页和前一页
- 2.shown.bs.tab -  标签页显示后触发。。使用event.target和event.relatedTarget来定位到激活的标签页和前一页

##### 代码:
```html
<script>
    $(function(){
        $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
            // 获取已激活的标签页的名称
            var activeTab = $(e.target).text();
            // 获取前一个激活的标签页的名称
            var previousTab = $(e.relatedTarget).text();
            $(".active-tab span").html(activeTab);
            $(".previous-tab span").html(previousTab);
        });
    });
</script>
```

## 6. Bootstrap提示工具(tooltip)插件
提示工具用于提醒页面访问者

### 6.1 用法
默认情况下把提示工具(tooltip)放到触发元素后面。 使用前，必须激活提示工具，激活代码:\$(function () { \$('.tooltip-show').tooltip('show');});。有以下两个方式添加提示工具:

- 1.通过data属性：向锚标签添加data-toggle="tooltip"。锚的title即为提示工具的文本。默认设置在顶部
- 2.通过JavaScript：如:\$('#identifier').tooltip(options)

### 6.2 选项
提供工具提供多个属性，帮助用户开发:

- 1.data-placement：指定提示位置，如palcement="left"。如果是"auto left"，则尽可能显示在左边，如果左边不允许，才显示在右边
- 2.title：提示工具的文本

##### 代码:
```html
<div class="myTooltip">
    <a href="#" data-toggle="tooltip" data-placement="auto top" title="是一个帅哥">thinking_fioa</a>
    <br>
    <a href="#" data-toggle="tooltip" data-placement="auto left" title="是一个美女">ppp</a>
</div>

<script>
    $(function () {
        $("[data-toggle='tooltip']").tooltip();
    });
</script>
```

### 6.3 方法
提示工具(Tooltip)插件中有用的方法:

- 1.tooltip(options) - 向元素集合附加提示工具句柄
- 2.tooltip('toggle') - 切换显示／隐藏元素的提示工具
- 3.tooltip('show') - 显示元素的提示工具
- 4.tooltip('hide') - 隐藏元素的提示工具
- 5.tooltip('destroy') - 隐藏并销毁元素的提示工具

##### 代码:
```html
$(function () { $('.tooltip-show').tooltip('show');});
```

### 6.4 事件
提示工具插件要用到的事件，如下:

- 1.show.bs.tooltip - 调用show实例方法，立即触发该事件
- 2.shown.bs.tooltip - 显示完成后，触发该事件
- 3.hide.bs.tooltip - 调用hide实例方法，理解触发该事件
- 4.hidden.bs.tooltip - 隐藏完成后，触发该事件

##### 代码:
```html
$(function () { 
	$('.tooltip-show').tooltip('show');
});
$(function () { 
	$('.tooltip-show').on('show.bs.tooltip', function () {
		alert("Alert message on show");
	})
});
```

### 7. Bootstrap 弹出框





















