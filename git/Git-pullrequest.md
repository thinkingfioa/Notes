# GitHub中PR(pull Request)操作
```
GitHub已经成为所有程序员的天堂和地狱。
众多程序员在此网站上活跃，想为开源贡献代码，就必须要学会提交PR。PR即是Pull Request操作
本人gitHub地址: https://github.com/thinkingfioa
```

## 1. 贡献代码
贡献代码，通俗的说，就是自己修改了代码，希望合并到别人的Repository(仓库)中。将自己的智慧贡献给开源社区。下面将详细讲解步骤

### 1.1 第一步:fork
在GitHub社区闲逛时，看中了某个项目代码，如：spring-projects/spring-framework，点击页面Fork按钮，会生成一个自己的Repository(仓库：thinkingfioa/spring-framework),如下图:

![](http://img.blog.csdn.net/20180311145019349?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

### 1.2 第二步：修改
fork成功后，通过git clone、修改、commit、push等操作后，将修改的内容，提交到自己仓库(thinkingfioa/spring-framework)中。如果对git clone、commit和push不知道的，自行百度。如下图:

![](http://img.blog.csdn.net/20180311145118818?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

### 1.3 第三步：请求合并代码(Pull Request)
在1.2步骤时，我们修改了自己的仓库(thinkingfioa/spring-framework)代码。我们希望贡献自己的一份力量，将修改的Commit也提交到别人的仓库(spring-projects/spring-framework)中。则要进行Pull Request。

##### 1.3.1 创建PR

![](http://img.blog.csdn.net/20180311145148985?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

##### 1.3.2 Create pull request
请特别注意下图中标红的部分，不能搞反了。点击: **Create pull request** 绿色按钮，完成提交PR。

![](http://img.blog.csdn.net/20180311145208969?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

##### 1.3.3 等待
提交PR完成后，等待对方仓库(spring-projects/spring-framework)的管理员审核，如果他同意，则贡献代码完成了。


## 2. 同步最新代码
PR除了贡献代码外，还可以同步对方最新代码。通俗的说，fork某个仓库(如: spring-projects/spring-framework)代码一段时间后，为了同步自己仓库(thinkingfioa/spring-framework)和对方仓库(spring-projects/spring-framework)代码，保证自己仓库代码是最新版本。

### 2.1 同步最新代码

##### 2.1.1 Create pull request
这一步和上面1.3.2一样的，只是要注意箭头，哪个仓库合并哪个仓库。请自习注意下图标红部分

![](http://img.blog.csdn.net/20180311145239737?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

###### 2.1.2 点击绿色按钮，完成同步
![](http://img.blog.csdn.net/20180311145252473?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdGhpbmtpbmdfZmlvYQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)










