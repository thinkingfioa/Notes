#第3章:对象的共享
```
本章目的:介绍如何共享和发布对象,从而使它们能够安全地多个线程同时访问.
```
```
要编写正确的并发程序,关键问题在于:在访问共享的可变状态时需要进行正确的管理
```
[TOC]

###3.1 可见性
```
同步还有另一个重要的方面:内存可见性.
也就是说,希望确保当一个线程修改了对象状态后,其他线程能够看到发生的状态变化.
```
```
内存可见性一个重要的Bug:无法确保执行读操作的线程能适时地看到其他线程写入的值.
```
- 举例:
```
NoVisibility类中,一个主线程希望通过变量的值,同事另一个线程,但是糟糕的是:失败!
```
```java
public class NoVisibility {
    private static boolean ready;
    private static int number;

    private static class ReaderThread extends Thread {
        public void run() {
            while (!ready)
                Thread.yield();
            System.out.println(number);
        }
    }
    public static void main(String[] args) {
        new ReaderThread().start();
        number = 42;
        ready = true;
    }
}
```
Note:
```
NoVisibility可能会持续下去,死循环.因为读线程可能永远也看不到ready的值.就是上面的内存可见性一个典型的BUG.
```
#######避免内存可见性问题
```
有一种简单的方法:只要有数据在多个线程之间共享,就使用正确的同步.一定要考虑,否则程序可能出现非常奇怪的问题.
```

#####3.1.1 失效数据
```
NoVisibility中展示了一个缺乏同步的程序可能出错的一种情况:失效数据.也就是读线程永远读到的是失效的值.
```
```
失效数据的出现,将会可能程序非常难以调BUG.请慎重,参考上面如何避免内存可见性问题的方法.
```
- 举例:
```java
@NotThreadSafe
public class MutableInteger {
    private int value;

    public int get() {
        return value;
    }

    public void set(int value) {
        this.value = value;
    }
}
```
Note:
```
MutableInteger是一个非线程安全的类.不仅具有竞态条件,同时也可能出现同步问题.
多线程时,可能通过调用get()方法,得到的值是一个失效的数据.
```
#######如何变成线程安全
```java
@ThreadSafe
public class SynchronizedInteger {
    @GuardedBy("this")
    private int value;

    public synchronized int get() {
        return value;
    }

    public synchronized void set(int value) {
        this.value = value;
    }
}
```

Note:
```
1. 将get方法,set方法都加上关键字synchronized.可以保证类SynchronizedInteger线程安全.
```
```
2. 但不能保证类SynchronizedInteger不会并发问题,缺可以保证类SynchronizedInteger同步
```
```
3. 如果仅仅对set方法进行同步也是不够的,因为调用get的线程仍然看见失效值.
```

#####3.1.2 非原子的64位操作.
```
当由于同步问题,可能线程读取到一个失效值,但这个值一定是之前某个线程设置的值,而不是一个随机值.这称为最低安全性.
```
```
有一个非常特殊的情况:非volatile类型的64位数值变量(double和long,参考3.1.4),JVM允许将64位的读操作或写操作分解为两个32位操作.
所以,多线程程序中使用可变的long和double等类型,那么没有关键字volatile则可能会存在并发问题,不安全.
```

##### 3.1.3 加锁与可见性
#######synchronzied关键字为什么能保证同步
```
当线程执行某个synchronized的代码块时,对其他线程是可见的,所以,不存在读取失效数据,可见性保证.
```
```
官方解释:在访问某个共享且可变的变量时要求所有线程在同一个锁上同步,就是为了确保某个线程写入该变量的值对于其他线程来说都是可见的.
```
```
加锁的含义不仅仅局限于互斥行为,还包括内存可见性.为了确保所有线程都能看到共享变量的最新值,
所有执行读操作或者写操作的线程都在同一个锁上同步.
```

#####3.1.4 Volatile变量
```
Volatile变量用来确保将变量的更新操作通知其他线程,读取Volatile类型的变量时总会返回最新写入的值.
```
####### 如何理解Volatile变量
```
将volatile修饰的变量,想象用synchronized关键字来理解,读操作和写操作分别用set方法和get方法.
```
```
不建议过度依赖volatile变量提供的可见性,volatile变量来控制状态的可见性,通常比使用锁的代码更脆弱,也更难理解.
```
#######Volatile使用条件
```
1. 加锁机制既可以确保可见性又可以确保原子性,而volatile变量只能确保可见性.
```
```
2. 对变量的写入操作不依赖变量的当前值,或者你能确保只有单线程更新变量的值.
```
```
3. 该变量不会与其他状态变量一起纳入不变性条件中.
```
```
4. 在访问变量时,不需要加锁.
```

### 3.2发布与逸出
```
封装的好处:封装能够使得对程序的正确性进行分析变得可能,并使得无意中破坏设计约束条件变得更难.
```
```
"发布"的意思是：是对象能够在当前作用域之外的代码中使用.
```
```
"逸出"的意思是:当一个不应该发布的对象被发布时,称为逸出.
```
```
对象的"发布"可能给该对象带来破坏.比如:如果在对象构造完成之前就发布该对象,就会破坏线程安全,后面会给出理由.
```
#####对象逸出的方法
```
1. 最简单的方法:将对象的引用保存到一个公有的静态变量中,以便任何类和线程都能看见该对象.
```
```
2. 当发布某个对象时,可能会间接地发布其他对象.
```
- 举例:

```java
public static Set<Secret> knownSecrets;

public void initialize(){
	knownSecrets = new HashSet<Secret>();
}
```
Note:
```
1. knownSecrets对象就是一个静态变量,所以被发布出去
2. 发布对象knownSecrets这个时,也将发布了对象Secret.因为任何代码都能遍历得到Secret对象.
```

```
3. 如果从非私有方法中返回一个引用,那么同样会发布返回的对象.
```
```
4. 发布对象或其内部状态机制就是发布一个内部的类实例.
```
- 举例:
```java
public class ThisEscape {
    public ThisEscape(EventSource source) {
        source.registerListener(new EventListener() {
            public void onEvent(Event e) {
                doSomething(e);
            }
        });
    }
}
```
Note:
```
ThisEscape发布EventListener时,也隐含的发布了ThisEscape实例本身,因为这个内部类的实例中包含了对ThisEscape实例的隐含引用(?)
```
#####安全的对象构造过程
```
不要在构造过程中使this引用逸出
```
```
当且仅当对象的构造函数返回时,对象才处于可预测和一致的状态.因此,当从对象的构造函数中发布对象时,只是发布一个尚未构造完成的对象.
```
```
构造过程中,使this引用逸出的一个常见错误是:构造函数中启动一个线程,这样this引用都会被新建的线程共享.
可以在构造函数中创建线程,但是请不要立即启动它,而是通过一个start或者initialize方法启动(第7章).
```
```
在构造函数中调用一个可改写的实例方法时,同样会导致this引用逸出.
```
#######使用工厂方法来防止this在构造过程中逸出
```java
public class SafeListener {
    private final EventListener listener;

    private SafeListener() {
        listener = new EventListener() {
            public void onEvent(Event e) {
                doSomething(e);
            }
        };
    }

    public static SafeListener newInstance(EventSource source) {
        SafeListener safe = new SafeListener();
        source.registerListener(safe.listener);
        return safe;
    }
}
```


