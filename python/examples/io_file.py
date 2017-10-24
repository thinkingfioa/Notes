#!/usr/bin/python
# -*- coding: UTF-8 -*-

fileObject = open("test_io_file.txt", "rb+")
#fileObject.write("gitHubAddress is https://github.com/thinkingfioa\n")
fileLine = fileObject.read()
print "context is : ", fileLine
fileObject.close()

str = raw_input("请输入: ")  # 输入: thinking
print "输入内容是：", str  # 输出: thinking


str2 = input("请输入: ")  # 输入: [x*5 for x in range(2,10,2)]
print "输入内容是：", str2  # 输出: [10, 20, 30, 40]