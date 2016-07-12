#第2章:线程安全性
[TOC]
```
要编写线程安全的代码,器核心在于要对状态访问操作进行管理,特别是共享和可变的状态.
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
#####2.2.1 竞争条件
```
竞争条件:在并发编程中,由于不恰当的执行时序而出现不正确的结果,统称为:竞争条件.
```











