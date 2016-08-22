# 第5章: 基础构建模块
```
本章目的:本章介绍Java类库中一些最有用的并发构建模块.及使用这些模块来构造并发应用程序时的一些常用模式
```
[TOC]

### 5.1 同步容器类
```
同步容器类包括:Vector和Hashtable.
实现线程安全的方式是:将它们的状态封装起来,并对每个公有方法都进行同步,是的每次只有一个线程能访问容器的状态
```

##### 5.1.1 同步容器类的问题
```
同步容器类是线程安全的,但是某些情况下可能需要额外的客户端加锁来保护复合操作.
常见的复合操作:迭代(遍历),"若没有则添加".
```
- 举例 1:
```
即使Vector是线程安全类,但是下面的例子任然非线程安全
```

```java
public static Object getLast(Vector list){
	int lastIndex = list.size() -1 ;
    return list.get(lastIndex);
}

public static void deleteLast(Vector list){
	int lastIndex = list.size() -1;
    list.remove(lastIndex);
}
```
Note:
```
上面的代码,在并发访问时,明显会出现并发错误.可能会抛出异常:ArrayIndexOutOfBoundsException异常
```
####### 解决方法
```
使用加锁机制:synchronized(this){...},保证原子性操作
```
- 举例 2:
```
Vector在进行遍历是也会出现上面的并发问题
```
```java
for(int i =0;i<vector.size();i++){
	doSomethinkng(vector.get(i));
}
```
Note:
```
相同的原因:因为另一个线程并发修改了Vector.解决方法:synchronized(vector){...}
```

##### 5.1.2 迭代器与ConcurrentModificationException
