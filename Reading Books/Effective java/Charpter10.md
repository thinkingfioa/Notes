#第10章:并发
[TOC]
```
本章目的:线程并发机制可以提高程序性能,但也存在较多困难.本章介绍基本并发程序开发技巧
```

###第66条:同步数据访问共享的可变数据
```
关键字synchronized可以保证同一时刻,只有一个线程可以执行某个方法,或者某个代码块
```
##### 同步
```
同步不仅可以阻止一个线程看到对象处于不一致的状态下之中,还可以保证进入同步方法或者同步代码块的每个线程,
都看到由同一个锁保护的之前所有的修改效果
```
```
如果没有同步,一个线程的变化就不能被其他线程看到
```

#####Java语言规范保证读或者写一个变量的原子性
```
读取一个非long或double类型的变量,可以保证返回的值是某个线程保存在该变量中的,也就是说,大家共享这个变量,并发的修改这个变量.但写入和读出都是原子性的.
```

#####对共享可变数据的访问不能保证同步的后果
```
后果很严重
```
- 举例:
```
下面的例子:阻止一个线程妨碍另一个线程的任务
```
```
Java类库提供了Thread.stop方法,但是这个方法很久就不提倡使用.因为Thread.stop方法不安全,会导致数据遭到破坏,所以请不要使用方法:
Thread.stop()
```
```
要阻止一个线程妨碍另一个线程,建议做法:
让第一个线程轮询(poll),这个域开始是false,但通过第二个线程设置为true,表示第一个线程将要终止自己.
```

#####阻止一个线程妨碍另一个线程的任务探讨
```java
// Broken! - How long would you expect this program to run ?
public class StopThread{
	private static boolean stopRequested;
    
    public static void main(String [] args) throws InterruptedException{
    	Thread backgroundThread = new Thread(New Runnable(){
        	public void run(){
            	int i = 0;
                while( ! stopRequested){
                	i++;
                }
            }
        });
        backgroundThread.start();
        
        TimeUnit.SECONDS.sleep(1);
        stopRequested = true;
    }
}
```
Note:
```
这段程序在我的机器是,始终循环.并不是预期一秒后结束
```
######始终循环的原因
```
由于没有同步,就不能保证后台线程何时看到主线程对stopRequested的值所做的改变.
```













