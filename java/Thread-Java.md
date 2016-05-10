# Java线程
[toc]

##(1)实现多线程代码

1. 继承Thread类
	- 启动方式:
 1. 继承 Thread类，并覆写Thread类中的run()方法
 2. 以start()方法执行
2. 实现Runnable接口
	- 启动方式:
 1. 实现Runnable接口，并覆写Runnable()类中的run()方法
 2. 将Runnable的子类，丢进Thread(Runnable)中启动
```java
	new Thread(new Runnable(){
	@Override
	public void run(){
    	//need thread do something
        ...
    }
	}).start();
```

3. 两者区别：继承Thread类，子类中的资源是独有的。实现Runnable接口，将这个子类丢进多个Thread类中启动时，子类的资源共享
4. 理解一些方法
 1. t.join() : 执行线程执行到`t.join()`,当前线程强制等待线程t执行完.
 2. yield()方法将一个线程的操作暂时让给其他线程执行

##(2)线程的同步与死锁
>由来：因为用的是实现Runnable接口的方法，则子类的资源是共享，所以出现非同步

#### 同步代码块：指定需要同步的对象,可以是this,也可以是某个Object
```java
synchronized (this){
	//设置同步代码块的操作
    ...
    //
}
```

#### 同步方法:将一个方法声明成同步方法
```java
public synchronized void sale(){
	//设置该方法为同步方法
    ...
    //
}
```

##(3)ExecutorService线程池来创建线程

####类 Executors
- public static ExecutorService newCacheThreadPool()
> Note:创建一个线程池，如果以前的线程可用，将重用，对于执行短期异步任务的程序，速度快
- public static ExecutorService newFixedThreadPool(int nThreads)
> Note:创建一个可重用的，数目固定的线程，以共享的无界队列来运行这些线程(主要是这个线程池可以在挂掉或者出异常的情况下，重新启动一个线程来执行接下去的任务)
- public static ExecutorService newSingleThreadExecutor()
> Note:创建一个可线程，以共享的无界队列来运行线程

####类ThreadFactory接口使用，可以避免每次new Thread(r)
```java
public enum DaemonThreadFactory implements ThreadFactory{
	INSTANCE;
    @Override
    public Thread newThread(final Runnable r){
    	Thread t= new Thread(r);
        t.setDaemon(true);
        return t;
    }
}
```

####类 ExecutorService : 启动线程
-submit(Runnable task) ： 可以有返回值的，执行Runnable
-execute(Runnable command) : 执行Runnable
-shutdown() ：新的任务不再接受了，以前的任务执行完，退出
-shutdownNow() : 清除所有的线程，包括等待的线程和试图去停止执行的task

####以线程池（ExecutorService , Executors）的方式程序示例
Class for DeamonThreadFactory
```java
package vlis;

import java.util.concurrent.ThreadFactory;

public enum DeamonThreadFactory implements ThreadFactory{
    INSTANCE;
    @Override
    public Thread newThread( final Runnable r){
        Thread t = new Thread(r);
      //  t.setDaemon(true);
        return t;
    }
}
```

```java
package vlis;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Client{
    public static void main(String args[]){
        final ExecutorService executor = Executors.newSingleThreadExecutor(DeamonThreadFactory.INSTANCE);
        executor.submit(new Runnable(){
            @Override
            public void run(){
                System.out.println("thinking_fioa");
            }
        });
        executor.shutdown();
    }
}
```
