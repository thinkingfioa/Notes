#第2章:线程安全性
[TOC]
```
要编写线程安全的代码,其核心在于要对状态访问操作进行管理,特别是共享和可变的状态.
对象的状态指存储在状态变量(实例域或静态域)
```

###2.1 什么是线程安全性
```
当多个线程访问某个类时,这个类始终都能表现出正确的行为.
```
- 举例:一个无状态的Servlet.无状态对象是线程安全的.
```
一个基于Servlet的因数分解服务,并逐渐扩展它的功能,同时确保它的线程安全性
```
```java
@ThreadSafe
public class StatelessFactorizer extends GenericServlet implements Servlet {

    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        BigInteger[] factors = factor(i);
        encodeIntoResponse(resp, factors);
    }
}
```
Note:
```
StatelessFactorizer类无状态,既不包含任何域,也不包含任何对其他类中域的引用.方法的状态都是基于线程栈上的局部变量.是一个线程安全类.
```

###2.2 原子性
```
为上例加上一个"命中计数器"来统计所处理的请求数量.
```
```java
@NotThreadSafe
public class UnsafeCountingFactorizer extends GenericServlet implements Servlet {
    private long count = 0;

    public long getCount() {
        return count;
    }

    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        BigInteger[] factors = factor(i);
        ++count; //读取,修改,写回
        encodeIntoResponse(resp, factors);
    }
}
```
Note:
```
类UnsafeCountingFactorizer线程不安全.++count并非是原子操作,需要同步才能在多线程中保证正确性.
```
#####2.2.1 竞态条件
```
竞争条件:在并发编程中,由于不恰当的执行时序而出现不正确的结果,统称为:竞态条件.
```
#######先检查后执行(可能出现并发问题)
```
首先观察某个条件是否为真,然后根据这个观察结果采用相应的动作.但事实时,观察和执行动作之间往往由于并发问题,观察结果可能变得无效.
```
#####2.2.2 示例:延迟初始化中的竞态条件
```
一个非常典型的延迟初始化案例:使用懒汉的单例模式,但是可能存在多次初始化问题
```
```java
@NotThreadSafe
public class LazyInitRace {
    private ExpensiveObject instance = null;

    public ExpensiveObject getInstance() {
        if (instance == null)
            instance = new ExpensiveObject();
        return instance;
    }
}
```
Note:
```
LazyInitRace存在一个典型的竞态条件:先观察instance == null,然后在初始化
```
```
可能存在的并发问题是:可能new ExpensiveObject();被重复初始化.而且每个线程执行,都要重新一次初始化.
```
#####2.2.2 复合操作
```
要避免竞态条件,就必须在线程修改该变量时,防止其他线程使用该变量.保持原子性.
```
```
将"先检查后执行"以及"读取-修改-写入"等操作统称为复合操作.
也就是说:复合操作是包含一组必须以原子方法执行的操作以确保线程安全性.
```
#######使用AtomicLong来确保线程安全
```java
@ThreadSafe
public class CountingFactorizer extends GenericServlet implements Servlet {
    private final AtomicLong count = new AtomicLong(0);

    public long getCount() {
        return count.get();
    }

    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        BigInteger[] factors = factor(i);
        count.incrementAndGet();//原子性
        encodeIntoResponse(resp, factors);
    }
}
```
Note:
```
Java提供Atomic*类,该类是线程安全类,所以保证了线程安全.
```

###2.3 加锁机制
```
当servlet添加更多的状态时,使用Atomic*类可能不够
比如:Servlet将计算结果缓存起来:最近执行因数分解的数值,以及分解结果
```
```java
@NotThreadSafe
public class UnsafeCachingFactorizer extends GenericServlet implements Servlet {
    private final AtomicReference<BigInteger> lastNumber
            = new AtomicReference<BigInteger>();
    private final AtomicReference<BigInteger[]> lastFactors
            = new AtomicReference<BigInteger[]>();

    public void service(ServletRequest req, ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        if (i.equals(lastNumber.get()))
            encodeIntoResponse(resp, lastFactors.get());
        else {
            BigInteger[] factors = factor(i);
            lastNumber.set(i);
            lastFactors.set(factors);
            encodeIntoResponse(resp, factors);
        }
    }
}
```
Note:
```
1. UnsafeCachingFactorizer不是线程安全的,存在竞态关系.
UnsafeCachingFactorizer需要维护一个不变性条件:lastFactors中的缓存因数之积应该等于lastNumber.
```
```
2. 在使用原子引用情况下，尽管对set方法的每次调用都是原子的，但仍然无法同时更新lastNumber,lastFactors.
由于每次修改一个变量，那么变量之间的约束性，就被破坏了。
```
```
3. 当某个类涉及多个变量时,如果考虑线程安全,必须考虑多个变量是否之间存在约束性,如果存在约束,一定要小心并发问题.
比如：lastNumber, lastFactors
```
#####2.3.1 内置锁:
```
第三章将会介绍加锁机制以及其他同步机制的另一个重要的方面:可见性
```
```
每个java对象都可作为实现同步的锁,这些锁被称作内置锁
```
```
同步代码块有两种方式:一种是作为锁的对象引用,另一种是作为锁保护的代码块.
```
```
如果每个方法以关键字:synchronized修饰,那么同步代码块的锁就是方法调用所在的对象this.
```
#######性能与线程安全
```
有时为了线程安全,引入锁,可能导致性能问题.比如下面的代码,并发性特别糟糕
```
```java
@ThreadSafe
public class SynchronizedFactorizer extends GenericServlet implements Servlet {
    @GuardedBy("this")
    private BigInteger lastNumber;
    @GuardedBy("this")
    private BigInteger[] lastFactors;

    public synchronized void service(ServletRequest req,
                                     ServletResponse resp) {
        BigInteger i = extractFromRequest(req);
        if (i.equals(lastNumber))
            encodeIntoResponse(resp, lastFactors);
        else {
            BigInteger[] factors = factor(i);
            lastNumber = i;
            lastFactors = factors;
            encodeIntoResponse(resp, factors);
        }
    }
}
```
Note:
```
在2.5节将会讨论这个并发程序为何并发性低,且如何解决
```
#####2.3.2 重入
```
内置锁是可以重入的,因此某个线程试图获得一个已经由自己持有的锁,请求就会成功.
```
#######关于父类与子类锁重入讨论
```java
public class Widget{
	public synchronized void doSomething(){
    	//...
    }
}

public class LoggingWidget extends Widget{
	public synchronized void doSomething(){
    	System.out.println("ppp");
        super.doSomething();
    }
}
```
Note:
```
需要注意的一点是:doSomething()方法上,关键字synchronized锁住的对象都是子类调用的对象this.
因为:synchronized修饰,那么同步代码块的锁就是方法调用所在的对象this.所以如果锁不可重入,那么就会死锁无法进行下去.
```
###2.4 用锁来保护状态









