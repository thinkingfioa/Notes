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
- 建议第一行书写PROJECT，这一行同时引入两个变量HELLO_BINARY_DIR和HELLO_SOURCE_DIR。cmake自动定义了两个变量PROJECT_BINARY_DIR和PROJECT_SOURCE_DIR
- message用于输出变量的值
- set 命令用来设置变量
- add_executable 告诉工程生成一个可执行文件
- add_library 则告诉生成一个库文件
- target_link_libraries(hello libhello)关联依赖库
- set_target_properties 重新命名库
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

### 三、 sample3 将源文件链接为库
在sample2基础上，将hello.cpp生成一个库，再使用

### 1. CMakeLists.txt解释
```
PROJECT(HELLO)
set(LIB_SRC hello.cpp)
set(APP_SRC main.cpp)
add_library(libhello ${LIB_SRC})
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello")
```
##### 解释
- set命令设置两个变量: LIB_SRC和APP_SRC
- add_library用来生成一个lib库
- target_link_libraries用来关联以来的库
- set_target_properties用来生成名称为libhello.a，而不是缺省名为liblibhello.a

### 四、多个目录的源文件
- 将main.cpp和hello.h／hello.cpp分别放到两个目录下
- 生成的可执行文件和编译的中间依赖库，放到对应的编译包中

#### 1. 顶层的CMakeLists.txt
```
project(HELLO)
add_subdirectory(src)
add_subdirectory(libhello)
```
##### 解释
- add_subdirectory添加两个子模块

#### 2. SRC目录下的CMakeLists.txt
```
include_directories(${PROJECT_SOURCE_DIR}/libhello)
set(APP_SRC main.cpp)
# 设置可执行文件输出的地址
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)
```
##### 解释
- include_directories用于指明头文件所在路径
- set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)可执行文件生成的目录

#### 3. LibHello目录下的CMakeList.txt
```
set(LIB_SRC hello.cpp)
add_library(libhello ${LIB_SRC})
# 设置lib输出的目录
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello")
```

##  安装
1. brew install cmake
2. cmake --version

## 参考链接
1. [cmake学习笔记](https://blog.csdn.net/dbzhang800/article/details/6314073)
