#awk,grep,sed
[TOC]

###awk
```
Awk简单的说就是把文件逐行的读入，以空格为默认分隔符，将每行切片，切开的部分再进行各种分析处理。
```
#####使用方法
```
awk '{pattern + action}' {filenames}
```
Note: 
- Pattern表示AWK在数据中查找的内容，Action是找到匹配内容的行后所执行的一系列命令。
- Pattern就是要表示的正则表达式，用斜杠**/**括起来

##### 三种调用awk的方式
```
1. 命令方式
 		awk [-F field-separator] 'commands' input-file(s)
        
其中commands是真正的awk命令，[-F域分隔符]是可选的。input-file(s)是待处理的文件。
在awk中，文件的每一行中，有域分隔符分开的每一项称为一个域。通常，在不指名-F域分隔符的情况下，默认的域分隔符是空格。
```
```
2. shell脚本方式

	将所有的awk命令插入一个文件，并使awk程序可执行，然后awk命令解释器作为脚本的首行，一遍通过键入脚本名称来调用。相当于shell脚本首行的：#!/bin/sh，换成：#!/bin/awk
```
```
3. 将所有的awk命令插入一个单独文件，然后调用：
		awk -f awk-script-file input-file(s)
其中，-f选项加载awk-script-file中的awk脚本，input-file(s)跟上面的是一样的。
```

#####入门实例
```
1. $	last -n 5 | awk '{print $1}'
wkq
wkq
wkq
reboot
wkq

Note:  awk的工作流程：读入有'\n'换行符分割的一条记录，然后按照指定的域分隔符进行域的划分，填充域。$0则表示所有的域,$1表示第一个域,$n表示第n个域。默认域分隔符是：“空白键”或“[tab]键”
```
```
2.$		cat /etc/passwd | awk -F : '{print $1}'
...
wkq
dnsmasq
sshd
usermetrics
clickpkg
mysql
rabbitmq

Note:  显示/etc/passwd的账户，使用的是awk + action示例，每一行都会执行action{print $1}. -F : 是定义域非分隔符为 ‘：’
```
```
3. $	cat /etc/passwd | awk -F : '{print $1"\t"$7}'
...
wkq	/bin/bash
dnsmasq	/bin/false
sshd	/usr/sbin/nologin
usermetrics	/bin/false
clickpkg	/bin/false
mysql	/bin/false
rabbitmq	/bin/false

Note:显示/etc/passwd的账户和账户对应的shell,而账户与shell之间以tab键分割
```
```
4. $	cat /etc/passwd | awk -F : 'BEGIN {print "name,shell"} {print $1","$7} END {print "mylover,/bin/panpingping"}'
name,shell
root,/bin/bash
...
usermetrics,/bin/false
clickpkg,/bin/false
mysql,/bin/false
rabbitmq,/bin/false
mylover,/bin/panpingping

Note:  先执行BEGIN，然后读取文件的每一行，做对应的输出，再执行END操作。
```
```
5. $	awk -F: '/^root/' /etc/passwd
root:x:0:0:root:/root:/bin/bash

Note:  搜索/etc/passwd以root关键字开头的所有行。这时一个pattern的使用示例，匹配上pattern(这里是^root)的行才会执行action(这里没有指定action动作)
```
```
6. $	awk -F : '/^root/{print $7}' /etc/passwd
/bin/bash

Note:搜索/etc/passwd有root关键字的所有行，并显示对应的shell。匹配上pattern(这里是^root)的行，然后执行action({print $7})。
```
#####awk内置变量

####### awk最常用的一些变量

|变量|作用|
|	:---:	|	:---:	|
|ARGC|命令行参数个数|
|ARGV|命令行参数排列|
|ENVIRON|支持队列中系统环境变量的使用|
|FILENAME|awk浏览的文件名|
|FNR|浏览文件的记录数|
|FS|设置输入域分隔符，等价于命令行 -F选项|
|NF|浏览记录的域的个数|
|NR|已读记录数|
|OFS|输出域分隔符|
|ORS|输出记录分隔符|
|RS|控制记录分隔符|
```
1. $	awk -F : '{printf("filename:%10s,linenumber:%s,columns:%s,linecontent:%s\n",FILENAME,NR,NF,$0)}' /etc/passwd
...
filename:/etc/passwd,linenumber:1,columns:7,linecontent:root:x:0:0:root:/root:/bin/bash
...

Note:  统计/etc/passwd：文件名，每行的行号，每列的列数，对应的完整行内容
```
#######print和printf区别
```
1. print函数的参数可以是变量，数值或者字符串。字符串必须用双引号引用，参数用逗号分隔。逗号的作用是与输出文件的分隔符的作用一样的，只是后者是空格。
2. printf的用法与C语言中使用方法一样。可以参考上面的例子。
```


#####awk编程
#######变量与赋值
```
1. $	awk 'BEGIN {count=0;print "[start]user count is ",count} {count=count+1;print $0} END {print "[end]user count is ",count}' /etc/passwd

[start]user count is  0
...
rabbitmq:x:120:130:RabbitMQ messaging server,,,:/var/lib/rabbitmq:/bin/false
...
[end]user count is  40

Note:  如果count没有初始化，会默认值为0
```
```
2. $	ls -l | awk 'BEGIN {size=0;} {size=size+$5} END {print "[end]size is ",size/1024/1024,"M"}'
[end]size is  13038.6 M

Note:  统计当前文件的总大小，单位为：M
```
#######条件语句：与C语言中是一样的
```
1. $	ls -l | awk 'BEGIN {size=0;} {if($5!=4096){size=size+$5;}} END{print "[end]size is ",size/1024/1024,"M"}'
[end]size is  13038.5 M

Note:  统计某个文件夹下的文件占用的字节数,过滤4096大小的文件(一般都是文件夹)
```
#######数组
		awk中数组的下标可以是数字和字母，数组的下标通常被成为关键字(key)。
```
1. $	awk -F : 'BEGIN {count=0;} {name[count]=$1;count++} END{for(i=0;i<NR;i++) print i, name[i]} '/etc/passwd'
0,root
1,daemon
...
38,mysql
39,rabbitmq
```

### grep
```
grep命令是一种强大的文本搜索工具，使用正则表示式搜索文本，并把匹配的行打印出来
```
#####正则表达式
|表达式|功能|
|:---:|:---:|
|\|忽略字符的原有含义|
|^|开始行字符|
|$|结束行字符|
|\<the|匹配以the开头的词的行|
|the\>|匹配以the结尾的词的行|
|[AB]|匹配具有A或B字符的词|
|[A-Z]|A,B,...,Z的所有都符合|
|.|所有的单个字符|
|*|所有的字符|
|?|最多匹配一次|
|*|匹配零次或者任意多次|
|.*|匹配任意多的字符|
|+|匹配一次以上|
|{n}|匹配n次|
|{n,}|最少匹配n次|
|{,m}|最多匹配m次|
|{n,m}|匹配n到m次|
#####入门实例
#######普通测试用例
```
测试文件demo_file
$	cat demofile
THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
This Line Has All Its First Character Of The Word With Upper Case.

Two lines above this line is empty.
And this is the last line.

AAA A bd safe afe sfe efa
a aAAAA bd safe afe sfe efa
```
```
1. 从单个文件中搜索指定的字符串
Usage:	grep "findString" filename

$	grep "this" demo_file
this line is the 1st lower case line in this file.
Two lines above this line is empty.
And this is the last line.
```
```
2. 在多个文件中检索指定的字符串
Usage:	grep "findString" demofile*
```
```
3. grep -i大小写无关的搜索
Usage:	grep -i "the" demo_file

THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
This Line Has All Its First Character Of The Word With Upper Case.
And this is the last line.
```
```
4.	使用正则表达式
Usage:	grep "REGEX" filename

$	grep "lines.*empty" demo_file
Two lines above this line is empty.
```
```
5.	grep -w 搜索整个词，而不是词的一部分，等价于:"\<findString\>"
Note
 1. 无 -w参数
$	grep -i "is" demo_file

THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
This Line Has All Its First Character Of The Word With Upper Case.
Two lines above this line is empty.
And this is the last line.
 2. 有 -w参数
$	grep -i -w "is" demo_file

THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
Two lines above this line is empty.
And this is the last line.
```
```
6.	grep -r递归搜索全部文件
$	grep -r -i "this" *

demo_file:THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
demo_file:this line is the 1st lower case line in this file.
demo_file:This Line Has All Its First Character Of The Word With Upper Case.
demo_file:Two lines above this line is empty.
demo_file:And this is the last line.
demo_file2:THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
demo_file2:this line is the 1st lower case line in this file.
demo_file2:This Line Has All Its First Character Of The Word With Upper Case.
demo_file2:Two lines above this line is empty.
demo_file2:And this is the last line.
grep2/demo_file1:THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
grep2/demo_file1:this line is the 1st lower case line in this file.
grep2/demo_file1:This Line Has All Its First Character Of The Word With Upper Case.
grep2/demo_file1:Two lines above this line is empty.
grep2/demo_file1:And this is the last line.
```
```
7.	grep -v进行不匹配
$	grep -v "go" demo_text

4. Vim Word Navigation

You may want to do several navigation in relation to the words, such as:


WORD - WORD consists of a sequence of non-blank characters, separated with white space.
word - word consists of a sequence of letters, digits and underscores.

Example to show the difference between WORD and word

 * 192.168.1.1 - single WORD
 * 192.168.1.1 - seven words.
```
```
8.	多个模式的使用 : -e
$	grep -i -e "go" -e "1" deom_text

 * e - go to the end of the current word.
 * E - go to the end of the current WORD.
 * b - go to the previous (before) word.
 * B - go to the previous (before) WORD.
 * w - go to the next word.
 * W - go to the next WORD.
 * 192.168.1.1 - single WORD
 * 192.168.1.1 - seven words.
```
```
9.	grep -c 统计匹配的行数

$	grep -c "go" demo_text
6
```
```
10.	grep -o只显示匹配的字符串，而不是原来的一行

$	grep -o "is.*line" demo_file
is line is the 1st lower case line
is line
is is the last line
```
```
11.	grep -b显示在整个文件中的字节 byte位置

$	grep -b -o "is.*line" demo_file
53:is line is the 1st lower case line
188:is line
212:is is the last line
```
```
12.	grep -n在输出时显示行号

$	grep -n -b -o "is.*line" demo_file
2:53:is line is the 1st lower case line
5:188:is line
6:212:is is the last line
```
#######高级示例
```
1.grep -A,-B and -C显示之前，之后，前后的几行
Note:创建文件demo_text
$	cat demo_text

4. Vim Word Navigation

You may want to do several navigation in relation to the words, such as:

 * e - go to the end of the current word.
 * E - go to the end of the current WORD.
 * b - go to the previous (before) word.
 * B - go to the previous (before) WORD.
 * w - go to the next word.
 * W - go to the next WORD.

WORD - WORD consists of a sequence of non-blank characters, separated with white space.
word - word consists of a sequence of letters, digits and underscores.

Example to show the difference between WORD and word

 * 192.168.1.1 - single WORD
 * 192.168.1.1 - seven words.

1.1 显示匹配行和之后的3行数据
$	grep -i -A 3 "example" demo_text

Example to show the difference between WORD and word

 * 192.168.1.1 - single WORD
 * 192.168.1.1 - seven words.

1.2 显示匹配行和之前的3行数据
$	grep -i -B "example" demo_text

WORD - WORD consists of a sequence of non-blank characters, separated with white space.
word - word consists of a sequence of letters, digits and underscores.

Example to show the difference between WORD and word

1.3 各显示前后N行
$	grep -i -C 2 "example" demo_text

word - word consists of a sequence of letters, digits and underscores.

Example to show the difference between WORD and word

 * 192.168.1.1 - single WORD
```
### sed