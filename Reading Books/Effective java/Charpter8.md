#第８章：通用程序设计
[TOC]
```
本章目的：讨论Java语言的具体细节，包括下面这几个部分
```
|本章讨论的内容|
|:---:|
|局部变量的处理|
|控制结构|
|类库的用法|
|各种数据类型的用法|
|反射机制与本地方法|
|优化和命名惯例|

###第45条：将局部变量的作用域最小化
```
将局部变量的作用域最小化，可以增强代码的可读性和可维护性，降低出错。本条目和第13条本质是一样的(13)
```
#####最有力的方法
```
1. 请在第一次使用的它的地方声明。如果声明太早，则不容易读。
```
```
2. 如果还没有足够的信息对一个变量进行有意义的初始化，应该推迟这个声明，直到可以初始化为止。
```
#######例外
```
如果一个变量被一个方法初始化且这个初始化方法可能抛出异常，同时try块的外部该变量也被使用。那么这个try块前，需要声明，但try块前，并不能被"有意义地初始化"。
```

#####循环中的变量作用域
```
for循环中允许声明循环变量，它们的作用域限制在循环体中。普遍的for循环方法(46)
```
```java
// Preferred idiom for iterating over a collection
for(Element e : c){
	doSomething(e);
}
```
#######推荐使用for循环，避免使用while循环
```
1. for循环中声明的变量，作用于仅限于循环体中，而while循环的控制变量，作用域很广。当遇到"剪贴-粘贴"时，极容易出错。
```
```
2. for循环简短，增强了可读性。
```
```
3. 有一种非常棒的写法，经常使用的
```
```java
for(int i =0,n = expensiveComputation();i<n;i++){
	doSomething(i);
}
```

#####还有一种方法得到本条目目的：是方法小而集中
```
另个方法合并，那么第一个方法的局部变量会在另一个操作的代码范围内有效。一个长方法是不被推荐的
```

###第46条：for-each循环优先于传统的for循环
#####传统的for循环举例
#######第一种
```java
//No longer the preferred idiom
for(Iterator i = c.iterator();i.hasNext;){
	doSomething((Element)i.next());
}
```
#######第二种
```java
for(int i=0;i<a.length;i++){
	doSomething(a[i]);
}
```
#####推荐使用的for-each循环
```java
//The preferred idiom for iterating
for(Element e : elements){
	doSomething(e);
}
```

#####推荐理由
```
1. 传统的for循环中，无论是迭代器或索引变量的变化性有程序员控制，容易错误。而且，出错并不容易发现。
```
```
2. 利用for-each循环不会有性能损失，而且容易理解。冒号(:)可以理解为"从里面取数据"
```
#######举例说明，传统for循环容易出错
```
1. 传统for循环，出现BUG
```
```java
// have a BUGGGGGGGGGGGGGGGGGGGGGG
for(Iterator<Face> i = faces.iterator();i.hasNext();){
	for(Iterator<Face> j = faces.iterator();j.hasNext();){
    	System.out.println(i.next() + " " + j.next());
    }
}
```
Note:
```
期望输出结果是一个全排列的结果，但是实际输出结果却不是。原因在于:i.next()变化影响的。
```
```
2. 采用for-each循环代码,思路清晰，不易出错。
```
```java
for(Suit suit: suits){
	for(Rank rank: ranks){
    	deck.add(new Card(suit, rank));
    }
}
```

#####感悟
```
如果你在编写一个类型表示的是一组元素，一定要考虑实现Iterable。这样用户就可以利用for-each循环遍历你的类型，她会深深爱上你的
```
#####总结
```
for-each循环的简洁性和预防Bug方面的优势巨大，但是遗憾的是，下面三种情况无法使用for-each循环
```
```
1. 过滤---如果需要遍历集合，并删除选定的元素，就需要显式的迭代器，因为需要调用remove方法
```
```
2. 转换---如果需要遍历列表或者数组，并修改它的部分或者全部的元素值，就需要列表迭代器或者数组索引，以便修改数据
```
```
3. 平行迭代---如果需要并行地遍历多个集合，需要显式控制迭代器或者索引变量，以便可以同步迁移。
```
```
如果可以使用for-each循环，请使用for-each循环。如果是上面三种情况，请留心本条目上面所提到的陷阱。
```

###第47条：了解和使用类库
