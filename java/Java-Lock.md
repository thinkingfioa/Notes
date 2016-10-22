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
2. 比如读文件,其实,多线程读文件是可以共享的,读写加锁,谢谢加锁即可.Synchronized同样无法办到,只能保证一个线程操作.Lock却可以.
```
```
3. Lock可以知道线程有没有成功获取到锁,但Synchronized无法办到.
```

#####Lock与Synchronized不同点
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
















