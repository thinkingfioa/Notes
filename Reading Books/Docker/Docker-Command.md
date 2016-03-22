#Docker使用的基本命令
[TOC]
###安装
```
请Google
```
###镜像
***
#####获取镜像
#######获取最新版本
```
1. sudo docker pull ubuntu
```
#######获取指定标签+特定版本镜像
```
2. sudo docker pull ubuntu:14.04
```
Note:如果不能pull成功，请修改/etc/hosts，加入域名指定解析
#######指定服务器仓库下载
```
3. sudo docker pull dl.dockerpool.com:5000/ubuntu
```
#####查看镜像信息
#######列出本地主机已有镜像
```
1. sudo docker images
```
#######为本地镜像添加新的标签
```
2. sudo docker tag oldRepository:oldTag newRepository:newTag
```
#######获取镜像的详细信息
```
3. sudo docker inspect ubuntu:14.04
```
#####搜索镜像
```
4. sudo docker search mysql
```
#####删除镜像
```
5. sudo docker rmi ubuntu:14.04
6. sudo docker rmi Id // 删除所有的tag的ID一样的镜像
```
#####创建镜像
#######基于已有镜像的容器创建
Note：使用docker commit命令
```
格式：sudo docker commit [OPEIONS] Container [Repository[:TAG]]
```
|OPTIONS|提示|
|:--:|:---:|
|-a|-\-author=""作者信息|
|-m|-\-message=""提交信息|
|-p|-\-pause=true提交时暂停容器运行|
- 举例
```
sudo docker commit -m "add a new file" -a "thinking_fioa" 361e0c18a975
```

#######基于本地模板导入
Note：直接从一个操作系统模板文件导入一个镜像
```
sudo cat ubuntu-14.04-x86_64-minimal.tar.gz | docker import - ubuntu:14.04
```
#####存出和载入镜像
#######存出镜像：将镜像存出到本地文件
```
sudo docker save -o ubuntu_14.04.tar ubuntu:14.04
```
#######载入镜像
```
sudo docker load < ubuntu_14.04.tar
```
#####上传镜像
Note：用户user上传本地的test:latest镜像，可以先添加新的标签user/test:latest，然后用docker push命令上传
命令格式:
```
sudo docker push NAME[:TAG]
```
- 举例:
```
sudo docker tag test:latest user/test:latest
sudo docker push user/test:latest
```
***
###容器
#####创建容器
#######新建容器
```
sudo docker create -it ubuntu:14.04 /bin/bash //不启动
```
#######新建并启动容器
```
sudo docker run -it ubuntu:14.04 /bin/bash
```
Note:

|命令参数|作用 |
|:---:|:---:|
|-t|分配一个伪终端|
|-i|容器的标准输入保持打开|
#######守护态运行
```
sudo docker run -d ubuntu:14.04 /bin/bash
```
Note: 可以使用命令 **sudo docker logs ContainerId** 来查看docker输出信息
#####启动、终止容器
#######启动容器
```
1. sudo docker start ContainerId
```
```
2. sudo docker restart ContainerId
```
#######终止容器
```
sudo docker stop ContainerId
```
#####进入容器
#######attach命令
```
sudo docker attach Namess
```
#######exec命令(推荐使用)
```
sudo docker exec -it ContainerId /bin/bash
```
#####删除容器
```
sudo docker rm ContainerId
```
|命令参数|作用|
|:---:|:---:|
|-f|--force=false强行终止并删除一个运行中的容器|
|-l|--link=false删除容器的连接,但保留容器|
|-v|--volumes=false删除容器挂载的数据卷|

#####导入和导出容器(容器的迁移时,使用)
#######导出容器
```
将已经创建的容器导入到一个文件
```
```
docker export ContainerId > test_for_run.tar
```
#######导入容器
```
将导出的文件使用docker import命令导入,成为镜像
```
```
cat test_for_run.tar | sudo docker import - test/ubuntu:v1.0
```

