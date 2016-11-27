# 保证线程或定时器活着
[TOC]

### 导言
```
开发中,经常使用到线程或定时器,但是,如何保证线程一直不死,捕捉线程异常.
```
```
参考文章:http://www.cnblogs.com/yuhuihong19941210/p/5547501.html
```

##### 线程异常捕捉
```
利用Thread提供的setUncaughtExceptionHandler捕捉异常.
```
```java
 public class ThreadCatchException {
 
     private ThreadTask task = new ThreadTask();
    
     public static void main(String[] args) {
         ThreadCatchException plan = new ThreadCatchException();
         plan.start();
     }
     public void start(){
         Thread thread = new Thread(task);
         thread.setUncaughtExceptionHandler(new UncaughtExceptionHandler(){
             @Override
             public void uncaughtException(Thread t, Throwable e) {
                 System.out.println(e.getMessage());
                 start();//重新启动
             }
         });
         thread.start();
     }
     
     class ThreadTask implements Runnable{
         private int task = 10;
         @Override
         public void run() {
           //Do something
         }
     }
 }
```

##### 线程池的异常捕捉
```
专门为线程池提供线程工厂,在创建线程的时候,提供具有setUncaughtExceptionHandler的线程.
这种方式只使用于execute(...),submit(...)方式请参考下面定时方式.
```
```java
public class ThreadPoolCatchException {
     private ThreadTask task = new ThreadTask();

	 private MyFactory factory = new MyFactory(task);
     public static void main(String[] args) {
         ThreadPoolCatchException plan = new ThreadPoolCatchException();
         ExecutorService pool = Executors.newSingleThreadExecutor(plan.factory);
         pool.execute(plan.task);
         pool.shutdown();
     }
     
     class MyFactory implements ThreadFactory{
         private ThreadTask task;
         public MyFactory(ThreadTask task) {
             super();
             this.task = task;
         }
         @Override
         public Thread newThread(Runnable r) {
             Thread thread = new Thread(r);
             thread.setUncaughtExceptionHandler(new UncaughtExceptionHandler() {
                 @Override
                 public void uncaughtException(Thread t, Throwable e) {
                     ExecutorService pool = Executors.newSingleThreadExecutor(new MyFactory(task));
                     pool.execute(task);
                     pool.shutdown();
                 }
             });
             return thread;
         }
     }
     
     class ThreadTask implements Runnable{
         private int task = 10;
         @Override
         public void run() {
            //do something
         }
     }
 }
```

##### 定时任务,异常捕捉
```
定时任务,一律废除Timer的使用.
```
```
Scheduled要利用future.get()方法来获取是否有异常出现
```
```java
public class ScheduledCatchException {
     private ScheduleTask task = new ScheduleTask();

	 public static void main(String[] args) {
         ScheduledCatchException plan = new ScheduledCatchException();
         start(plan.task);
     }
     
     public static void start(SimpleTask task){
         ScheduledExecutorService pool = Executors.newSingleThreadScheduledExecutor();
         ScheduledFuture<?> future = pool.scheduleAtFixedRate(task, 0, 1000, TimeUnit.MILLISECONDS);
         try {
             future.get();
         } catch (InterruptedException | ExecutionException e) {
             start(task);
         }finally {
             pool.shutdown();
         }
     }
     
     class ScheduleTask implements Runnable{
         private volatile int count = 0;
         @Override
         public void run() {
             //do something
         }
     }
}

```