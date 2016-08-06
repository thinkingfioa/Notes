# 第4章:对象的组合
```
本章目的:介绍一些组合模式,这个模式能够使一个类更容易成为线程安全.并且维护这些类不会无意中破坏类的安全性保证.
```
[TOC]

### 4.1 设计线程安全类
```
使用封装技术,可以在不对整个程序进行分析的情况下,判断一个类是否线程安全.所以,推荐封装.
```
```
私有变量和共有共有静态域相比,私有变量封装性更好,在线程并发情况下,更容易保证线程安全.
```
##### 设计线程安全类的三个基本要
```
1. 找出构成对象状态的所有变量
```
```
2. 找出约束状态变量的不变性条件
```
```
3. 建立对象状态的并发访问管理策略
```
#######对象状态的分析
```
1. n个基本类型对象,其状态就是域构成的n个元组
```
```
2. 对象的域是引用,那么状态也包含引用对象的域.比如:链表的状态是所有节点对象的状态.
```
```java
@ThreadSafe
public final class Counter {
    @GuardedBy("this")
    private long value = 0;

    public synchronized long getValue() {
        return value;
    }

    public synchronized long increment() {
        if (value == Long.MAX_VALUE)
            throw new IllegalStateException("counter overflow");
        return ++value;
    }
}
```
Note:
```
状态只有value变量来控制.
```
```
3. 同步策略:定义了如何在不违背对象不变条件或后验条件的情况下对其状态的访问操作进行协同.
```

#####4.1.1 收集同步需求
```
并发情况下,需要保证类的不变性条件和后验条件.比如:不可变条件,Counter类中,value必须大于0.
后验条件:下一个状态依赖于当前状态,当前值是17,下一个值是18.
```
```
由于不变性条件以及后验条件在状态及状态转换上施加各种约束,因此需要额外的同步与封装.
```

#####4.1.2 依赖状态的操作
```
类的不变性条件和后验条件约束了在对象上有哪些状态和状态转换是有效的.但还有一种先验条件
```
```
先验条件:依赖状态的操作,比如:队列移除某个元素时,需要队列不空.并发程序需要考虑先验条件.
```
```
想实现某个等待先验条件为真时才执行的操作,Java提供类库(阻塞队列[Blocking Queue]或信号量或其他的同步工具)
```

#####4.1.3 状态的所有权
```
C++中对所有权特别强调:把一个对象传递个某个方法,必须考虑是否传递对象的所有权,短期所有权还是长期.
```
```
很多时候,所有权和封装是相互关联的.比如:某个对象被封装到一个类中,则该类具有这个对象的所有权,需要对这个对象的并发访问负责.
```
```
容器类通常表现出一种"所有权分离"的形式.也就是说,容器类拥有其自身的状态,而客户代码具有容器中各个对象的状态.
```

###4.2 实例封闭
```
封装提供一种实例封闭机制,简化线程安全类的实现过程.
```
```
将数据封装在对象内部,可以将数据的访问限制在对象的方法上,更容易确保线程安全.
但要注意的一点是:被封闭的对象不能逸出
```
#####对象封闭
```
1. 对象可以封闭在类的一个实例上(作为类的私有成员)
```
```
2. 对象可以封闭在某个作用域内(作为一个局部变量)
```
```
3. 封闭在一个线程内(比如:将对象从一个方法传递到另一个方法内,必须是同一个线程)
```
- 举例:

```java
@ThreadSafe
public class PersonSet {
    @GuardedBy("this")
    private final Set<Person> mySet = new HashSet<Person>();

    public synchronized void addPerson(Person p) {
        mySet.add(p);
    }

    public synchronized boolean containsPerson(Person p) {
        return mySet.contains(p);
    }
}
```
Note:
```
HashMap并不是线程安全的,但是mySet被封闭到PersonSet类中,唯一的访问路径被内置锁保护,所以这是一个线程安全的类.
```
```
需要提醒:如果Person是可变的,那么mySet将Person逸出时,还需要额外的同步.
```
#####装饰器
```
Java内库中提供很多的线程封闭示例,唯一的用途就是将非线程安全的类转化为线程安全类.
比如:Collections.synchronizedList为ArrayList提供线程安全装饰器.
```
```
装饰器只是接口中每个方法实现为同步方法,并将调用请求转发到底层的容器上.
```

##### 4.2.1 Java监视器模式
```
Java监视器模式会把对象的所有可变状态都封装起来,并由对象自己的内置锁来保护.比如:Counter类
```
```
第11章将介绍如何通过细粒度的加锁策略来提高可伸缩性.Java监视器模式主要优势:简单.
```
```
锁可以是内置锁,也可以是私有锁
```
- 举例:
```java
public class PrivateLock {
    private final Object myLock = new Object();
    @GuardedBy("myLock")
    Widget widget;

    void someMethod() {
        synchronized (myLock) {
            // Access or modify the state of widget
        }
    }
}
```
Note:
```
与使用内置锁相比,私有的锁对象可以保证客户代码无法得到锁,但客户代码可以通过公有方法访问锁.
```

##### 4.2.2 示例:车辆追踪
```
下面举例,关于java监视器模式的示例:一个用于调度车辆的"车辆追踪器"
```
```
每台车都有一String的对象作为标识,并且拥有相应的坐标(x,y).
会有一个视图线程用于显示车辆位置,多个更新操作线程执行更新.
```
```
视图线程与执行更新操作的线程将并发的访问数据模型,因此需要并发.
```
```java
public class MonitorVehicleTracker {
    @GuardedBy("this")
    private final Map<String, MutablePoint> locations;

    public MonitorVehicleTracker(Map<String, MutablePoint> locations) {
        this.locations = deepCopy(locations);
    }

    public synchronized Map<String, MutablePoint> getLocations() {
        return deepCopy(locations);
    }

    public synchronized MutablePoint getLocation(String id) {
        MutablePoint loc = locations.get(id);
        return loc == null ? null : new MutablePoint(loc);
    }

    public synchronized void setLocation(String id, int x, int y) {
        MutablePoint loc = locations.get(id);
        if (loc == null)
            throw new IllegalArgumentException("No such ID: " + id);
        loc.x = x;
        loc.y = y;
    }

    private static Map<String, MutablePoint> deepCopy(Map<String, MutablePoint> m) {
        Map<String, MutablePoint> result = new HashMap<String, MutablePoint>();

        for (String id : m.keySet())
            result.put(id, new MutablePoint(m.get(id)));

        return Collections.unmodifiableMap(result);
    }
}

@NotThreadSafe
public class MutablePoint {
    public int x, y;

    public MutablePoint() {
        x = 0;
        y = 0;
    }

    public MutablePoint(MutablePoint p) {
        this.x = p.x;
        this.y = p.y;
    }
}
```
Note:
```
1. 尽管MutablePoint是线程安全,但是MutablePoint类封装在MonitorVehicleTracker类中
```
```
2. deepCopy方法,为了保证线程安全,必须返回一个Collections.unmodifiableMap(map),而且,Map中的对象必须是复制的一份.二者,缺一不可.
```
```
3. 实现的方式是通过返回客户代码之前复制可变的数据来维持线程安全.但是,如果车辆容器非常大的情况下可能有极大的性能问题
性能问题解释:dedpCopy是从一个synchronized方法中调用,因此执行时间较长的复制操作.当有大量车辆需要追踪时,锁保证了每次只有一个线程访问.
```

### 4.3 线程安全性的委托.
