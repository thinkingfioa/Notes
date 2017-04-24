# ScheduledThreadPoolExecutor使用
[TOC]

### Timer缺陷,请用ScheduledThreadPoolExecutor替代
```
1. Timer时间依赖于系统时间.机器时间更换,那么Timer将会不工作
```
```
2. Timer多个执行任务时,第一个任务失败了,所有任务都不会执行,因为后台是用线程维护的.
```
```
3. Timer执行多个任务,如果第一个任务在规定时间内没有完成,那么将会影响其他任务执行,后台只会启动一个线程.
```

### ScheduledThreadPoolExecutor
#####方法介绍
####### scheduleAtFixedRate(Runnable command,long initialDelay,long period,TimeUnit unit)
```
这个方法,时间概念非常强,运行时间也在周期时间内.运行时间点:initialDelay + period * n;
如果规定时间未完成,则下次任务立即执行.
```

####### scheduleWithFixedDelay(Runnable command,long initialDelay,long delay,TimeUnit unit)
```
时间概念比较浅,每次运行完后,在等待delay时间后在运行.所以,运行时间不包括在delay中.
```

##### ScheduledThreadPoolExecutor使用
```
ScheduledThreadPoolExecutor可以解决以上Timer所有的缺陷.
```
```java
public class ScheduledThreadPool{
	ScheduledExecutorService scheduledThreadPool = Executors.newScheduledThreadPool(5);
    
    WorkerThread worker = new WorkerThread();
    
	public static void main(String [] args){
    	start();
    }
	public static start(){
    	
 		scheduledThreadPool.schedule(worker, 10, TimeUnit.SECONDS);
    }
    
    public static void stop(){
    	scheduledThreadPool.cancle();
        scheduledThreadPool.shutdown;
    }
    
    public class WorkerThread implements Runnable{
   		 @Override
   		 public void run() {
         	//do something
  		  }
	}
}
```









