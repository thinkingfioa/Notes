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









































