include_directories(${PROJECT_SOURCE_DIR}/libhello)
set(APP_SRC main.cpp)
# 设置可执行文件输出的地址
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
add_executable(hello ${APP_SRC})
target_link_libraries(hello libhello)