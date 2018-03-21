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
Bootstrap插件提供了纯JavaScript方式的API。如:$(".btn.danger").button("toggle").addClass("fat");

### 1.3 事件
Bootstrap提供两种形式的事件:

- 1.动词不定式：在事件开始时被触发。能够在事件开始前停止操作的执行。例如ex:show
- 2.过去分词形式：在动作执行完毕后被触发。例如ex:shown

































