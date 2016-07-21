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
3. 入股仅仅对set方法进行同步也是不够的,因为调用get的线程仍然看见失效值.
```

#####3.1.2 非原子的64位操作.




