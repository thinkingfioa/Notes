set(LIB_SRC hello.cpp)
add_library(libhello ${LIB_SRC})
# 设置lib输出的目录
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set_target_properties(libhello PROPERTIES OUTPUT_NAME "hello")