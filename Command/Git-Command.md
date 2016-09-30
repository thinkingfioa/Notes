#git
###配置SSH KEY
```
1. $	ssh-keygen -t rsa -C "thinking_fioa@163.com
```
```
2. 将~/.ssh/id_rsa.pub的内容复制到github账户上
```
###git使用表格
|命令|作用|
|:---:|:---:|
|git clone address|复制代码库到本地|
|git add fileName |添加文件到代码库中|
|git rm fileName |删除代码库的文件|
|git commit -m <message>|提交更改，在修改了文件以后，使用这个命令提交修改|
|git pull|从远程同步代码库到本地|
|git push|推送代码到远程代码库|
|git branch|查看当前分支。带*是当前分支|
|git branch branchName|新建一个分支|
|git branch -d <branch-name>|删除一个分支|
|git checkout <branch-name>|切换到指定分支|
|git log|查看提交记录（即历史的 commit 记录）|
|git status|当前修改的状态，是否修改了还没提交，或者那些文件未使用|
|git diff filename|查看具体修改的内容|
|git reset HEAD filename|恢复原来的内容|
|git reset log|恢复到历史版本|
|git init|将当前目录初始化为本地仓库|
|git checkout|丢弃本地修改|

###git命令的使用

#####用户设置(本质:修改home目录下的.gitConfig文件)
```
$	git config --global user.name "thinkingfioa"
$	git config --global user.email "thinking_fioa@163.com"
```

#####从版本库中删除文件
```
$	git rm test.txt
$	git commit -m "remove test.txt"
```

#####误删文件,但版本库中还有,可以恢复
```
$	git checkout -- < filename >
```

#####丢弃本地修改,回到本地库版本
```
$	git checkout -- < filename >
```
#####查看本机库与远程库之间区别
```
1. 取回本地
$	git fetch origin
```
```
2. 比较不同
$	git diff master(local) origin/master
```
```
3. merge
$	git merge origin/master
```
#####对修改文件进行提交
```
1. git add fileName
```
```
2. git commit -m "desription"
```
##### git的push使用
```
git push origin local:remote
```
##### git的pull使用
```
git pull origin remote:local
```

#####git对commit撤销
```
1. 查看commit的id
$	git log
```
```
2. 撤销commit
$	git reset --hard commid_id
```
#####将本地目录文件上传远程仓库
```
Note:将本地目录文件上传全新远程仓库
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/thinkingfioa/gitExam.git 
// Or git remote add origin git@github.com:thinkingfioa/gitExam.git
git push -u origin master
```
```
Note:将本地目录文件上传已经存在远程仓库
git remote add origin git@github.com:thinkingfioa/gitExam.git
git push -u origin master
```

#####git 分支

#######查看分支
```
$	git branch
```

#######创建一个新的分支
```
$	git branch newbranchname
```

####### 切换分支
```
$	git checkout newbranchname
```
####### 创建+切换分支
```
$	git checkout -b newbranchname
```
####### 合并分支到当前分支
```
$	git merge branchname
```
#######删除分支
```
$	git branch -d branchname
```
#####回滚
```
git reset HEAD filename
```
#####拷贝仓库到本地
```
$	git colne git@github.com:thinkingfioa@RepositoryName
```
#####添加文件到代码库中
```
$	git add fileName
```
#####提交更改
```
$	git commit -m "description information"
```
#####将本地的commit信息,推送到github代码仓库
```
$	git push -u origin master
```
