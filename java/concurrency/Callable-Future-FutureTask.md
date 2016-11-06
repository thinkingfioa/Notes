# Callable-Future-FutureTask
[TOC]

### Callable和Runnable
##### java.lang.Runnable, 无法返回任务执行结果
```java
public interface Runnable{
	public abstract void run();
}
```
##### java.util.concurrent.Callable<V> 可以返回执行结果
```java 
public interface Callable<V>{
	V call() throws Exception;
}
```
####### 如何使用Callable<V>
```
在ExcutorService接口中提供submit方法重载
```
```java
<T> Future<T> submit(Callable<T> task);
<T> Futrue<T> submit(Runnable task, T result);
Futrue<?> submit(Runnable task);
```
Note:
```
第一个submit方法和第三个submit方法常用.
```

### Future
```
Future就是对于具体的Runnable或者Callable任务的执行结果进行取消、查询是否完成、获取结果.
```
##### Futrue作用
```
1. 判断任务是否完成
2. 能够中断任务
3. 获取任务执行结果.
```
##### java.util.concurrent.Future
```java
public interface Future<V> {
    boolean cancel(boolean mayInterruptIfRunning);
    boolean isCancelled();
    boolean isDone();
    V get() throws InterruptedException, ExecutionException;
    V get(long timeout, TimeUnit unit)
        throws InterruptedException, ExecutionException, TimeoutException;
}
```
##### Future几种方法解释
#######cancel方法
```
mayInterruptIfRunning = true时,表示可以取消正在执行过程中的任务.
```
```
cancel方法返回true时,表示取消成功.如果任务取消.
```
#######isCancelled方法
```
表示任务是否被取消成功,如果取消成功,则返回true;
```
#######isDone方法
```
表示任务是否已经完成，若任务完成，则返回true
```
#######get()
```
获取执行结果，会一直等到任务执行完毕才返回,所以会产生阻塞，
```
#######get(long timeout, TimeUnit unit)
```
获取执行结果，如果在指定时间内，还没获取到结果，就直接返回null
```

### FutrueTask
##### java.util.concurrent.FutureTask
```java
public class FutureTask<V> implements RunnableFuture<V>

public interface RunnableFuture<V> extends Runnable, Future<V> {
    void run();
}
```

### 使用示例
```java
public class Test{
	public static void main(String [] args){
    	ExecutorServer exec = Executors.newCacheThreadPool();
        Future<Integer> futureResult = exec.submit(new Callable<Integer>(){
        	@Override
            public Integer call() throws Exception{
            	Thread.sleep(3000);
        		int sum = 0;
        		for(int i=0;i<100;i++)
          	  	sum += i;
        		return sum;
            }
       });
       
       // get Result from Future
       try{
       		Integer integer = futureResult.get();
       } catch (InterruptedException e) {
            e.printStackTrace();
       } catch (ExecutionException e) {
            e.printStackTrace();
       }
    }
}
```

### 提醒
```
当使用executor.submit(task)时,要注意,可能线程执行速度太慢,导致线程已经满了,可以采用了默认的饱和策略.所以需要注意异常.
```
```java
try{
	futureResult = exec.submit(task);
    result = futureResult.get(time, timeUtil);
}catch(RejectedExecutionException rejEx){

}
```

### 几种饱和策略
##### AbortPolicy
```
中止(Abort)策略,是默认的饱和策略.该策略抛出未检查的RejectedExecutionException
```
##### CallerRunnsPolicy
```
这是一个非常特殊的策略,不会抛弃任务,也不会抛出异常,而是将任务回退给调用者,也就是任务提交者来做.这样减少任务提交速度.
```
##### DiscardPolicy
```
悄悄的抛弃该任务
```
##### DiscardOldestPolicy
```
抛弃在队列中待最久的任务
```

