# Vim命令+配置
## vim基础命令

### 通常使用命令

|命令|功能|
|:---:|:---:|
|:q!|退出|
|:e filename|打开一个文件|
|:x|Write file(if changes has been made) and exit|
|:sav filename|saves file as filename|
|.|Repeats the last change mode in normal mode|
|x|删除光标的位置的字符|
|A|跳转到改行末尾，进入编辑模式|
|a|跳转到单词末尾，进入编辑模式|
|0|跳转到改行首|
|$|跳转到改行末尾|

### 文件中移动的命令

|命令|功能|
|:---:|:---:|
|CTRL+f|向前滚动一页|
|CTRL+b|向后滚动一页|
|CTRL+u|向前滚动半页|
|CTRL+d|向后滚动半页|
|CTRL+g|显示当前光标所在的行和文件状态信息|
|G|移动光标到文件末尾|
|gg|移动光标到文件开头|
|e|移动光标到单词结束的位置|
|w|移动光标到下一个单词开始的位置|
|b|移动光标到单词开始的位置|
|0|回到行首|
|:33|跳转到33行|
|%|跳转到对应的配对的括号|

### 删除类命令

- 输入 **dw**  可以从光标处删除一个单词至单词末尾
- 输入 **d$**  从当前光标删除至行末
- 输入 **dd** 可以删除整个一行

### 计数指定动作次数

- 在动作之前输入次数，表示执行的次数

```
输入 2w 表示光标向前移动两个单词
输入  0（数字零）移动光标到行首
```

- 输入 d number(数字) motion 数字将会使操作执行多次

```
d2w表示删除 2个单词
输入 2dd 则表示删除两整行
```

### 撤销类命令

- 输入  **u** 则表示撤销最近执行的命令
- 输入  **U**  则表示撤销对一行修改
- 输入   **ctrl+R**  来撤销掉撤销的命令

### 置入类命令

- 输入 **p** 将最后一次删除的内容置入光标后（如果上次删除的是一行，则会把该行置入当前光标所在行的下一行）
- 输入 **r** 和一个字符，将替换光标所在的位置的字符
- 输入 **R**，则可以连续替换多个字符
- 输入 **cw** 将会删除光标至单词末尾，同事进入插入模式  
 - **c**与**d**的差别在于：**c**会进入编辑模式


### 搜索类命令

|命令|功能|
|:---:|:---:|
|/word|Search word from top to bottom|
|?word|Search word from bottoml to top|
|*|Search the word under cursor|
|/\cstring|Search STRING or string,case insensitive|
|/jo[ha]n|Search john or joan|
|/\<the|搜索以the开头的单词|
|/\<the\>|Search the|
|/fred\|joe|Search fred or joe|
|/^b\{2}|搜索以bb开头的行|
|/^\n\{3}|Find 3 empty lines|
|:bufdo /searchstr|Search in all open files|
|:bufdo %s/something/somethingelse/g|Search something in all the open buffers and replace it with somethingelse|
|n|Jump to next target|
|N|jump to pre target|


### 替换命令

|命令|功能|
|:---:|:---:|
|:s/old/new/|替换该命令的光标所在的行的第一个匹配的|
|:s/old/new/g|替换当前的光标所在的行的|
|:%s/old/new/g|Replace all occurences of old by new in file|
|:%s/onward/forward/gi|Replace onward by forward,case unsensitive|
|:%s/old/new/gc|Replace all occurences with confirmation|
|:2,35s/old/new/g|Replace all occurences between lines 2 and 35|
|:5,$s/old/new/g|Replace all occurences line 5 to EOF|
|:%s/^/hello/g|Replace the beginning of each line by hello|
|:%s/$/Bye/g|Replace the end of each line by Bye|
|:%s/ *$//g|Delete all white spaces|
|:g/string/d|Delete all lines containing string|
|:v/string/d|Delete all lines containing which didn't contain string|


### 在VIM类执行外部命令的方法

- 输入 **:!外部shell命令**

```
:!ls
```

### 读写文件

|命令|功能|
|:---:|:---:|
|:1,10 w outfile|Saves lines 1 to 10 in outfile|
|:1,10 w >> outfile|Appends lines 1 to 10 to outfile|
|:r infile|Insert the content of infile|
|:23r infile|Insert the content of infile under line 23|

- 输入先输入**v**会出现高亮部分，然后在输入** w  lu.txt **，则把高亮的部分保存到lu.txt 中

### 提取和合并文件

- 输入 **：r  lu.txt** ，则会将文件内容复制进入当前光标的位置处
- 输入 **：r !ls **，则会将ls命令的输出复制进入当前光标的位置处

### 附加类命令

- 输入 **a** ,则在光标之后插入文本

###剪贴，拷贝

|命令|功能|
|:---:|:---:|
|y|Copy the selected text to clipboard|
|p|Paste clipboard contents|
|dd|剪贴当前行|
|yy|拷贝当前行|
|y$|Copy to end of line|
|D|Cut to end of line|

- 使用方式：通常线输入 v 然后高亮想复制的，再输入 y,进行复制，再输入 p粘贴

###设置类命令的选项

- 举例说明：搜索类
    1. 输入  /ignore 进行搜索字符串  ignore,
    2. 输入  :set ic,则表示忽略大小写
    3. 输入  :set noic,则表示解除忽略大小写
    4. 输入  :set hls is,则表示高显搜索的词
    5. 输入  :set nohis nois,取消高显搜索的词

### 打开类命令

- 输入 **o**,则会在当前光标下方打开一行
- 输入 **O**,则会在当前光标上方打开一行   

### vim命令模式下模式下提示

- 输入 **CTRL+D**,会出现相关提示符号
- 输入 **TAB**键，补全命令

### 命令帮助

- 输入 **:help cmd**,出现命令的帮助
- 输入 **CTRL + W **，窗口的跳转vim_

###vim配置
#####显示行号
```
在目录:/etc/vim的文件夹下，修改文件vimrc,末尾加上**:set number**
```
