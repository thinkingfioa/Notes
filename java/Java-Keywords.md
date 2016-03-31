#Java关键字
[TOC]
###Java继承关系关键字

#####**static**关键字

#######static修饰的变量---父子(class : Father,Son)关系
```
1. Father类中有的 static 修饰的变量value,会被Son类继承下来,并可以在客户端Son.vlaue直接使用
2. Father类中有的 static 修饰的方法public static void Print(),也会被Son类继承下来,并可以直接使用
3. Son类如果OverrideFather的 static 变量或方法,则是正常的覆盖
4. Son类中声明每个域是static静态变量，则该变量属于类所有。
```

#######static修饰的变量---父子(interface : Father,class : Son)关系
```
1. 如果是static与上面的(class : Father,Son)是一样的
2. 注意:interface是不能有static修饰的方法,即使是没有实现也不行
```

#####**default**关键字
```
1. 如果某个类用修饰符default修饰的类，其他的包是不能引用的。怎么都不能用,即使反射都不行.
2. 如果某个类用修饰符default修饰的方法，其他的包是不能引用的。
```

###Java中，并发关键字
#####**volatile**关键字
```
volatile是java中并发处理中,使用的关键字。但不能保证原子性和同步性.其基本原理:线程1,线程2都需要用到 volatile修饰的变量Count,当前的Count=5.所以线程1,线程2都取到Count = 5,线程1对其进行修改成6,写回内存.线程2也对其修改成6.那么Count没有实现原子性操作.
```
