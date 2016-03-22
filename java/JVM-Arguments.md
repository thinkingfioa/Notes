#JVM-Argument
[TOC]
###JAVA启动内存大小参数
```
JAVA_OPTS="-Xms1024m -Xmx=1024m -XX:PermSize=512m -XX:MaxPermSize=512m"
```
###JAVA启动Jar包
```
JAVA_OPTS=${JAVA_OPTS}" -javaagent:/path"
```
###提供可以远程连接JVM配置的
```
JAVA_OPTS=${JAVA_OPTS}" -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=1105 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=10.10.101.33 " 
```
###JVM命令使用
#####得到当前程序线程整个情况
```
$	jstack [-l] pid
```
#####得到JVM的GC情况
```
$	jstat -gcutil pid
```
#####java中内存使用信息
|命令|作用|
|:---:|:---:|
|jmap pid|打印内存使用信息|
|jmap -heap pid|java heap 信息|
|jmap -histo:live pid|统计对象count ，live表示在使用|
|jmap -histo pid|各个有多少个对象占了多少内存的信息|
|jmap -dump:format=b,file=dumpFileName pid|生成dump文件|