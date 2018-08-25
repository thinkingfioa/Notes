# git使用手册
### 配置SSH KEY
```
1. $	ssh-keygen -t rsa -C "thinking_fioa@163.com
```
```
2. 将~/.ssh/id_rsa.pub的内容复制到github账户上
```

### git使用表格
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
|git branch -d branch-name|删除一个分支|
|git checkout branch-name|切换到指定分支|
|git log|查看提交记录（即历史的 commit 记录）|
|git status|当前修改的状态，是否修改了还没提交，或者那些文件未使用|
|git diff filename|查看具体修改的内容|
|git reset HEAD filename|恢复原来的内容|
|git reset log|恢复到历史版本|
|git init|将当前目录初始化为本地仓库|
|git checkout|丢弃本地修改|
|git push origin --delete branch-name|删除远程分之|
|git stash|保存当前分支所有未提交的修改，用于后续恢复当前工作目录|
|git stash pop|恢复之前git stash保存的修改|

### git命令的使用

##### 非常有用命令: git stash
开发过程中，经常出现当前开发分支是工作分支(work_branch)，但是开发功能还未开发完成，或者未充分提测，不想提交到git远程仓库。这是，测试人员和你说需要在develop分支上紧急fix掉一个小问题。由于当前分支(work_branch)未提交修改，无法切分支。此时，git stash派上用场。如下步骤：

1. git stash ------ 保存当前分支所有未提交的修改
2. git checkout develop ----- 切到develop分支，fix掉bug
3. git checkout work_branch ----- 切回原来的开发分支
4. git stash pop ----- 恢复之前git stash保存的修改

##### 如果发现.gitignore中无效,使用下面的命令
```
git rm -r --cached FileOrDirName
```

##### 用户设置(本质:修改home目录下的.gitConfig文件)
```
$	git config --global user.name "thinkingfioa"
$	git config --global user.email "thinking_fioa@163.com"
```

##### 从版本库中删除文件
```
$	git rm test.txt
$	git commit -m "remove test.txt"
```

##### 误删文件,但版本库中还有,可以恢复
```
$	git checkout -- < filename >
```

##### 丢弃本地修改,回到本地库版本
```
$	git checkout -- < filename >
```
 
##### 查看本机库与远程库之间区别
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

##### 对修改文件进行提交
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

##### git对commit撤销
```
1. 查看commit的id
$	git log
```
```
2. 撤销commit
$	git reset --hard commid_id
```

##### 将本地目录文件上传远程仓库
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

##### 查看分支
```
$	git branch
```

##### 创建一个新的分支
```
$	git branch newbranchname
```

##### 切换分支
```
$	git checkout newbranchname
```

##### 创建+切换分支(但是从当前本地分支切出)
```
$	git checkout -b newbranchname
```

##### 创建+切换分支(本地新建分支，从远程指定分支拉取)
```
$	git checkout -b newbranchname origin/远程分支名
```

##### 合并分支到当前分支
```
$	git merge branchname
```

#####删除分支
```
$	git branch -d branchname
```

##### 回滚
```
git reset HEAD filename
```

##### 拷贝仓库到本地
```
$	git colne git@github.com:thinkingfioa@RepositoryName
```

##### 添加文件到代码库中
```
$	git add fileName
```

##### 提交更改
```
$	git commit -m "description information"
```

##### 将本地的commit信息,推送到github代码仓库
```
$	git push -u origin master
```

##### 远程回滚方法
```
1. 先运行命令,git reset --hard commid_id, 回到某个commit_id上
2. 运行命令: git push -f远程强行回滚
```

##### 常用的.gitignore文件共享
```
*.class
*/.idea/
.idea/
/.DS_Store
*.iml
/target/
```
