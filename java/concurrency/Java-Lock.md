# Java并发编程:Lock
[TOC]

### Synchronized 不足
```
Synchronized是Java语言内置特性.如果一个线程获取了对应的锁,其他线程只能等着,等待获取锁的线程释放锁.
```
##### Synchronized两种情况下释放锁
```
1. 获得锁的线程执行完该代码块,然后线程释放锁的占有.
```
```
2. 拥有锁的线程抛出异常,JVM会让线程释放锁.
```
##### Synchronized几点缺点,Lock却提供更多的功能.
```
1. 如果一个线程由于等待IO或者其他原因(比如调用sleep方法)被阻塞了,但是又没有释放锁,其他线程只能等待.但是Lock提供一种机制,不让线程一直无限期的等待下去.
```
```
2. 比如读文件,其实,多线程读文件是可以共享的,读写加锁即可.Synchronized同样无法办到,只能保证一个线程操作.Lock却可以.
```
```
3. Lock可以知道线程有没有成功获取到锁,但Synchronized无法办到.
```

##### Lock与Synchronized不同点
```
1. Lock不是Java语言内置的，synchronized是Java语言的关键字,Lock是一个类，通过这个类可以实现同步访问
```
```
2. Lock需要手动释放锁,但synchronized缺不会.
```

### java.util.concurrent.locks包下常用类.

##### Lock类
```
Lock是一个借口类.
```
```java
public interface Lock {
    void lock();
    void lockInterruptibly() throws InterruptedException;
    boolean tryLock();
    boolean tryLock(long time, TimeUnit unit) throws InterruptedException;
    void unlock();
    Condition newCondition();
}
```

##### Lock类中四种加锁区别
```
Lock类中,lock(),tyrLock(),tryLock(long time, TimeUtil unit),lockInterruptible()四种加锁机制
```
####### lock()方法
```
1. lock()方法是平常使用最多的一个方法,就是用来获取锁,如果锁已经被其他线程获取,则进行等待.
```
```
2. 使用lock()方法需要注意,Lock机制需要主动释放锁,并且异常情况下也是这样.
所以,Lock必须在try{}catch{}块中,释放锁的操作放在finally块中,以保证锁一定被释放.
```
```java
Lock lock = ...;
lock.lock();//加锁.
try{
	//do something
}catch(Exception ex){

}
finally{
	lock.unlock();//释放锁
}
```
####### tryLock()方法
```
tryLock()方法是有返回值,用来表示尝试获取锁是否成功,如果成功返回true,失败则返回false;
也就是说,这个方法不管获取到锁或没有,都会返回,不会等待.
```
```java
Lock lock = ...;
if(lock.tryLock()){
	try{
    	//do something
    }catch(Exception ex){
    
    }finally{
    	lock.unlock(); 
    }
}else{
	//如果不能获得锁,直接做其他事.
}
```
####### tryLock(long time, TimeUnit unit)方法
```
tryLock(long time, TimeUnit unit)方法和tryLock()方法类似,区别在于,这个方法拿不到锁,会等待一定的时间,期限之内如果还拿不到,则返回false;
```
####### lockInterruptibly方法
```
当使用lockInterruptibly方法来获取线程时,如果线程正在等待锁,该线程允许被中断线程的等待状态.
也就是说,当线程A,B同时通过lock.lockInterruptibly()想获取某个锁时,线程A获得锁,所以线程B只能等待,那么对线程B调用threadB.interrupt()方法能够中断线程B的等待.
```
```java
public void method() throws InterruptedException{
	lock.lockInterruptibly();
    try{
    	//do something
    }finally{
    	lock.unlock();
    }
}
```
Note:
```
需要注意的是,当一个线程获取到锁之后,是不会被interrupt()方法中断的.
也就是说单独调用interrupt()方法不能中断正在运行过程的线程,只能中断阻塞过程的线程.
```
```
lockInterruptibly()方法获取某个锁时,如果获取不到,则会在等待,并且可以响应线程中断信号.
但是synchronized修饰的话,当一个线程等待某个锁时,是无法被中断的,只有一直等待下去.
```

### ReentrantLock是唯一一个实现Lock接口类.
```
ReentrantLock类是一个"可重入锁",实现了Lock类,且提供更多的方法
```
##### 举例使用ReentrantLock类
####### lock()
```java
public class Test{
	private ArrayList<Integer> arrayList = new ArrayList<Integer>();
    private Lock lock = new ReentrantLock();//必须是同一个变量
    
    public void main(String [] args){
    	final Test test = new Test();
        
        for(int i = 0;i<5){
        	new Thread(){
        		@Override
        	    public void run(){
        	    	test.insert(Thread.currentThread());
       		    }
     	   }.start();
        }
    
    public void insert(Thread thread) {
        lock.lock();//加锁,
        try {
            System.out.println(thread.getName()+"得到了锁");
            for(int i=0;i<5;i++) {
                arrayList.add(i);
            }
        } catch (Exception e) {
            // TODO: handle exception
        }finally {
            System.out.println(thread.getName()+"释放了锁");
            lock.unlock();//释放锁
        }
    }
}
```

####### tryLock()使用方法
```java
public class Test{
	private ArrayList<Integer> arrayList = new ArrayList<Integer>();
    private Lock lock = new ReentrantLock();//必须是同一个变量
    
    public void main(String [] args){
    	final Test test = new Test();
        
        for(int i = 0;i<5){
        	new Thread(){
        		@Override
        	    public void run(){
        	    	test.insert(Thread.currentThread());
       		    }
     	   }.start();
        }
    
    public void insert(Thread thread) {
        if(lock.tryLock()) { //加锁,
        	try {
           		System.out.println(thread.getName()+"得到了锁");
          		for(int i=0;i<5;i++) {
                	arrayList.add(i);
            	}
        	} catch (Exception e) {
            	// TODO: handle exception
        	}finally {
            	System.out.println(thread.getName()+"释放了锁");
            	lock.unlock();//释放锁
        	}
        }else{
        	System.out.println(thread.getName()+"获取锁失败");
        }
    }
}
```

####### lockInterruptibly()使用方法
```java
public class Test{
	private Lock lock = new ReentrantLock();
    public static void main(String [] args){
    	Test test = new Test();
        
        MyThread thread1 = new MyThread(test);
        MyThread thread2 = new MyThread(test);
        thread1.start();
        thread2.start();
        
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        thread2.interrupt();
        
        public void insert(Thread thread) throws InterruptedException{
        	lock.lockInterruptibly();//不可放到下面的try{}catch{}中
            try{
            	System.out.println(thread.getName()+"得到了锁");
            	while(true){}
            }finally{
            	System.out.println(Thread.currentThread().getName()+"执行finally");
            lock.unlock();
            System.out.println(thread.getName()+"释放了锁");
            }
        }
    }
}

class MyThread extends Thread{
	private Test test = null
    public MyThread(Test test){
    	this.test = test;
    }
    @Override
    public void run(){
    	try{
        	test.insert(Thread.currentThread())[]
        }catch(InterruptedException e){
        	System.out.println(Thread.currentThread().getName()+"被中断");
        }
    }
}
```
Note:
```
只有阻塞的线程才会响应interrupt()信号,运行的线程不会响应.
```

### ReadWriteLock类
```
ReadWriteLock类提供两个方法:readLock(),writeLock()方法
```
```java
public interface ReadWriteLock{
	Lock readLock();
    Lock writeLock();
}
```
Note:
```
ReadWriteLock类提供读写锁,将读写锁分开.
```

### ReentrantReadWriteLock类
```
ReentrantReadWriteLock类实现了ReadWriteLock接口类.
ReentrantReadWriteLock类提供了丰富的方法,但是最主要的方法:readLock()和writeLock()来获取读锁和写锁.
```
##### 实现读写文件锁机制
####### synchronized机制
```
不用说,肯定是并发操作,但是读与读操作也是原子性,可能会导致严重影响性能.
```
####### 使用ReentrantReadWriteLock类
```
允许同时读的操作,但是需要提醒的是,这个文件读操作,可能存在饥饿情况.
比如:众多读线程在操作文件,一个写线程过来,但是必须等待所有的读线程都结束后,才开始操作,所以可能会饥饿.
```
```java
public class Test{
	private ReentrantReadWriteLock rw1 = new ReentrantReadWriteLock();
    public static void main(String [] args){
    	final Test test = new Test();
        
        for(int i = 0;i<4;i++){
        	new Thread(){
            	@Override
                public void run(){
                	test.get(Thread.currentThread());
                }
            }.start();
        }
    }
    public void get(Thread thread) {
        rwl.readLock().lock();
        try {
            long start = System.currentTimeMillis();
            while(System.currentTimeMillis() - start <= 1) {
                System.out.println(thread.getName()+"正在进行读操作");
            }
            System.out.println(thread.getName()+"读操作完毕");
        } finally {
            rwl.readLock().unlock();
        }
    }
}
```

### Lock和Syschronized比较与选择
##### 比较
```
1. Lock是一个接口，而synchronized是Java中的关键字，synchronized是内置的语言实现；
```
```
2. synchronized在发生异常时，会自动释放线程占有的锁，因此不会导致死锁现象发生；而Lock在发生异常时，如果没有主动通过unLock()去释放锁，则很可能造成死锁现象，因此使用Lock时需要在finally块中释放锁；
```
```
3. Lock可以让等待锁的线程响应中断，而synchronized却不行，使用synchronized时，等待的线程会一直等待下去，不能够响应中断；
```
```
4. 通过Lock可以知道有没有成功获取锁，而synchronized却无法办到。
```
```
5. Lock可以提高多个线程进行读操作的效率。
```

##### 选择
```
在性能上来说，如果竞争资源不激烈，两者的性能是差不多的，
而当竞争资源非常激烈时（即有大量线程同时竞争），此时Lock的性能要远远优于synchronized。所以说，在具体使用时要根据适当情况选择。
```
