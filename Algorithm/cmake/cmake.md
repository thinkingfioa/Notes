# CMake使用说明

## 基础语法

## 手把手教学
|例子|说明|
|:---:|:---|
|sample1|单个源文件main.cpp|
|sample2|分解为main.cpp和hello.h/hello.cpp|
|sample3|先生成静态库，然后链接该库|
|sample4|将源文件放到不同的目录下|
|sample5|控制生成的程序和库所在的目录|
|sample6|使用动态库|

### 一、sample1 单个源文件

### 1. 源代码
单个main.cpp文件,利用CMakeLists.txt编译，建议创建一个build子目录，在子目录下调用cmake
```
main.cpp
#include <stdio.h>
int main() {
    printf("hello world\n");
    return 0;
}

CMakeLists.txt
project(HELLO) 
# message(${PROJECT_SOURCE_DIR})
set(SRC_LIST main.cpp)
add_executable(hello ${SRC_LIST})
```
##### CMakeLists.txt解释
- 建议第一行书写PROJECT，这一行同时引入两个变量HELLO_BINARY_DIR和HELLO_SOURCES_DIR。cmake自动定义了两个变量PROJECT_BINARY_DIR和PROJECT_SOURCES_DIR
- message用于输出变量的值
- set 命令用来设置变量
- add_executable 告诉工程生成一个可执行文件
- add_library 则告诉生成一个库文件
- CMakeLists.txt不区分大小写

### 2. 运行
- cd build
- 运行: cmake .. -G"Unix Makefiles"，将会在build目录下生成可执行文件hello

### 二、sample2 分解多个文件

### 1. 源代码
代码文件分为main.cpp和hello.h／hello.cpp
```
main.cpp
#include "hello.h"

int main() {
    hello(" thinking_fioa");
}

hello.h
#ifndef HELLO_
#define HELLO_
void hello(const char* name);
#endif // HELLO_

hello.cpp
#include <stdio.h>
#include "hello.h"

void hello(const char* name) {
    printf("Hello %s\n", name);
}

CMakeLists.txt
PROJECT(HELLO)
set(SRC_LIST main.cpp hello.cpp)
add_executable(hello ${SRC_LIST})
```

### 2. 运行
与sample1类似，不再解释.
- cd build
- 运行: cmake .. -G"Unix Makefiles"，将会在build目录下生成可执行文件hello

##  安装
1. brew install cmake
2. cmake --version

## 参考链接
1. [cmake学习笔记](https://blog.csdn.net/dbzhang800/article/details/6314073)
