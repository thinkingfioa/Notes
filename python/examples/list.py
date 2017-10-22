#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {"Name": "thinking", "age":18, "lover":"ppp"}
print dict  #输出 {'age': 18, 'Name': 'thinking', 'lover': 'ppp'}
del dict["lover"]
print dict  #输出 {'age': 18, 'Name': 'thinking'}
dict.clear()
del dict
print "-----------------------------"

list = ["thinking", "fioa", 123, 456]
print list # 输出: ['thinking', 'fioa', 123, 456]
del list[2]
print list # 输出: ['thinking', 'fioa', 456]

list2 = ["thinking", "fioa", 123, 456]
print list2[2]  # 输出 123
print list2[-3]  # 输出 fioa
print list2[1:]  # 输出 ['fioa', 123, 456]

list = [ "runoob", 786 , 2.23, "john", 70.2 ];
tinylist = [123, "john"];

print(list); #输出: ['runoob', 786, 2.23, 'john', 70.2]
print(list[0]); #输出: runoob
print(list[1:3]); #输出: [786, 2.23]
print(list[2:]); #输出: [2.23, 'john', 70.2]
print(tinylist *2 ); #输出: [123, 'john', 123, 'john']
print(list + tinylist); #输出: ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']



tuply = [ "runoob", 786 , 2.23, "john", 70.2 ];
tinytuply = [123, "john"];

print(tuply); #输出: ['runoob', 786, 2.23, 'john', 70.2]
print(tuply[0]); #输出: runoob
print(tuply[1:3]); #输出: [786, 2.23]
print(tuply[2:]); #输出: [2.23, 'john', 70.2]
print(tinytuply *2 ); #输出: [123, 'john', 123, 'john']
print(tuply + tinytuply); #输出: ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']


dict = {};
dict["one"] = "This is one";
dict[2] = "This is two";

tinydict = {"name": "john", "code":6734, "dept":"sales"};

print(dict["one"]); # 输出: This is one
print(dict[2]); # 输出: This is two
print(tinydict); # 输出: {'dept': 'sales', 'code': 6734, 'name': 'john'}
print(tinydict.keys()); # 输出: ['dept', 'code', 'name']
print(tinydict.values()); # 输出: ['sales', 6734, 'john']

a = 7;
b = 2;

list = [1,2,3,4,5];

if(a in list):
	print("a is in list");
else:
	print(" a is not list"); # 输出

if(b in list):
	print("b is in list"); # 输出
else:
	print("b is not list");


c = 10;
d = 7;


if(c is d):
	print("c is d"); # 输出
else:
	print("c is not d"); 

d = 10;

if(c is d):
	print("c is d"); 
else:
	print("c is not d"); # 输出