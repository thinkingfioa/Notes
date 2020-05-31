## 建议加上，改行引入两个变量: HELLO_BINARY_DIR和HELLO_SOURCE_DIR
# 通过cmake自动定义两个变量: PROJECT_BINARY_DIR和PROJECT_SOURCE_DIR
project(HELLO) 
# message用于输出变量的值
message(${PROJECT_SOURCE_DIR})
# set设置变量的值
set(SRC_LIST main.cpp)
# add_exectuable 告诉工程生成一个可执行文件
add_executable(hello ${SRC_LIST})