# linux下命令
[TOC]
### 命令汇总

##### 文件操作
|命令|作用|
|:---:|:---:|
|df -hl|查看磁盘信息|
|du -hs dirName|查看具体目录大小|
|du -hd1 dirName|查看目录层次为1的文件夹|
|ln sourcePath targetPath|硬连接后台指向同一个iNode|
|ln -s sourcePath targetPath|软连接，源只是存了目的目录的地址|
|tail -200f fileName|动态看文件内容|
|chown -R thinking:thinking fileName|改变文件或文件夹归属|
|chmod 744 fileName|改变文件权限|
|tar -czvf fileName.tar.gz sourceName|压缩|
|tar -xzvf fileName.tar.gz|解压缩|
|unzip|zip解压缩|
|find 当前目录 -name "fileName" -type d/f -print|在当前目录查找指定文件名+文件类型|

##### 系统管理命令
|命令|作用|
|:---:|:---:|
|who|显示登录用户|
|last|显示最近登录用户|
|date -s "20170909 06:00:00"|更新机器时间|
|uname -a|查看操作系统详细|
|free -tm|查看内存使用情况|
|vmstat|虚拟机运行情况|
|lsof -i:6669|查看端口占用|
|netstat -anp|查看所有端口占用情况|
|cat /proc/cpuinfo| grep "processor"| wc -l|查看逻辑CPU的个数|

##### 软件安装
|命令|作用|
|:---:|:---:|
|apt-get install|ubuntu 安转软件|
|apt-get search|ubuntu 搜索软件|
|apt-get remove|ubuntu 移除软件|
|brew install|mac 安装软件|
|brew search|mac 搜索软件|
|brew uninstall|mac 移除软件|
