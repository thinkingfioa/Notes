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
3. 如果仅仅对set方法进行同步也是不够的,因为调用get的线程仍然看见失效值.
```

#####3.1.2 非原子的64位操作.
```
当由于同步问题,可能线程读取到一个失效值,但这个值一定是之前某个线程设置的值,而不是一个随机值.这称为最低安全性.
```
```
有一个非常特殊的情况:非volatile类型的64位数值变量(double和long,参考3.1.4),JVM允许将64位的读操作或写操作分解为两个32位操作.
所以,多线程程序中使用可变的long和double等类型,那么没有关键字volatile则可能会存在并发问题,不安全.
```

##### 3.1.3 加锁与可见性
#######synchronzied关键字为什么能保证同步
```
当线程执行某个synchronized的代码块时,对其他线程是可见的,所以,不存在读取失效数据,可见性保证.
```
```
官方解释:在访问某个共享且可变的变量时要求所有线程在同一个锁上同步,就是为了确保某个线程写入该变量的值对于其他线程来说都是可见的.
```
```
加锁的含义不仅仅局限于互斥行为,还包括内存可见性.为了确保所有线程都能看到共享变量的最新值,
所有执行读操作或者写操作的线程都在同一个锁上同步.
```

#####3.1.4 Volatile变量
```
Volatile变量用来确保将变量的更新操作通知其他线程,读取Volatile类型的变量时总会返回最新写入的值.
```
####### 如何理解Volatile变量
```
将volatile修饰的变量,想象用synchronized关键字来理解,读操作和写操作分别用set方法和get方法.
```
```
不建议过度依赖volatile变量提供的可见性,volatile变量来控制状态的可见性,通常比使用锁的代码更脆弱,也更难理解.
```
#######Volatile使用条件
```
1. 加锁机制既可以确保可见性又可以确保原子性,而volatile变量只能确保可见性.
```
```
2. 对变量的写入操作不依赖变量的当前值,或者你能确保只有单线程更新变量的值.
```
```
3. 该变量不会与其他状态变量一起纳入不变性条件中.
```
```
4. 在访问变量时,不需要加锁.
```

### 3.2发布与逸出
```
封装的好处:封装能够使得对程序的正确性进行分析变得可能,并使得无意中破坏设计约束条件变得更难.
```
```
"发布"的意思是：是对象能够在当前作用域之外的代码中使用.
```
```
"逸出"的意思是:当一个不应该发布的对象被发布时,称为逸出.
```
```
对象的"发布"可能给该对象带来破坏.比如:如果在对象构造完成之前就发布该对象,就会破坏线程安全,后面会给出理由.
```
#####对象逸出的方法
```
1. 最简单的方法:将对象的引用保存到一个公有的静态变量中,以便任何类和线程都能看见该对象.
```
```
2. 当发布某个对象时,可能会间接地发布其他对象.
```
- 举例:

```java
public static Set<Secret> knownSecrets;

public void initialize(){
	knownSecrets = new HashSet<Secret>();
}
```
Note:
```
1. knownSecrets对象就是一个静态变量,所以被发布出去
2. 发布对象knownSecrets这个时,也将发布了对象Secret.因为任何代码都能遍历得到Secret对象.
```

```
3. 如果从非私有方法中返回一个引用,那么同样会发布返回的对象.
```
```
4. 发布对象或其内部状态机制就是发布一个内部的类实例.
```
- 举例:
```java
public class ThisEscape {
    public ThisEscape(EventSource source) {
        source.registerListener(new EventListener() {
            public void onEvent(Event e) {
                doSomething(e);
            }
        });
    }
}
```
Note:
```
ThisEscape发布EventListener时,也隐含的发布了ThisEscape实例本身,因为这个内部类的实例中包含了对ThisEscape实例的隐含引用(?)
```

#####安全的对象构造过程
```
不要在构造过程中使this引用逸出
```
```
当且仅当对象的构造函数返回时,对象才处于可预测和一致的状态.因此,当从对象的构造函数中发布对象时,只是发布一个尚未构造完成的对象.
```
```
构造过程中,使this引用逸出的一个常见错误是:构造函数中启动一个线程,这样this引用都会被新建的线程共享.
可以在构造函数中创建线程,但是请不要立即启动它,而是通过一个start或者initialize方法启动(第7章).
```
```
在构造函数中调用一个可改写的实例方法时,同样会导致this引用逸出.
```
#######使用工厂方法来防止this在构造过程中逸出
```java
public class SafeListener {
    private final EventListener listener;

    private SafeListener() {
        listener = new EventListener() {
            public void onEvent(Event e) {
                doSomething(e);
            }
        };
    }

    public static SafeListener newInstance(EventSource source) {
        SafeListener safe = new SafeListener();
        source.registerListener(safe.listener);
        return safe;
    }
}
```

### 3.3 线程封闭
```
一种避免同步的方式就是不共享数据,如果仅在单线程内访问数据,就不需要同步.这种技术被称为线程封闭.
```
#####使用线程封闭的例子
#######swing中大量使用线程封闭
```
Swing的可视化组件和数据模型对象都不是线程安全的,Swing将它们分发到线程中来实现线程安全性.
```
#######JDBC中的著名的Connection对象也使用线程封闭技术
```
大多数的请求(例如Servlet请求或EJB调用等)都是由单线程采用同步方式来处理,每次从线程池中获得一个Connection对象,
用来处理请求,用完归还给线程.
```
##### 3.3.1 Ad-hoc 线程封闭
```
Ad-hoc 线程封闭是指:维护线程封闭性的职责完全由程序来承担.Ad-hoc 线程封闭是非常脆弱的.
```
```
通常决定使用线程封闭技术时,通常是因为要将某个特定的子系统实现为一个单线程子系统.
```
####### volatile变量存在一种特殊的线程封闭.
```
只要能确保单个线程对共享的volatile变量执行写入操作.那么就可以安全的在这些共享的volatile变量执行"读取-修改-写入"的操作.
解释:单线程写入,保证了防止发生竞态条件,volatile变量的可见性保证其他线程可以看到最新的值.
```

##### 3.3.2 栈封闭
```
局部变量的固有属性之一就是封闭在执行线程中.它们位于执行线程的栈中,其他线程无法访问这个栈.
```
- 举例:
```java
public int loadTheArk(Collection<Animal> candidates){
	SortedSet<Animal> animals;
    int numPairs = 0;
    Animal candidate = null;
    
    //anaimals 被封闭在线程方法中,不要使它们逸出
    animals = new TreeSet<Animal> (new SpeciesGenderComparator());
    anamals.addAll(candidate);
    for(Animal a : anminals){
    	if(candidate == null || !candidate.isPotentialMate(a)){
        	candidate = a;
        }else{
        	ark.load(new AnimalPair(candidate, a));
            ++numPairs;
            candidate = null;
        }
    }
    return numPairs;
}
```
Note:
```
numPairs是基本类型引用,也是属于局部变量,所以,永远线程安全.
```
```
anaimals也是局部变量,但是是引用类型,要注意方式逸出.程序员需要特别小心这种引用类型的局部变量,如果发布引用类型的局部变量,
会导致对象animals逸出.
```

##### 3.3.3 ThreadLocal类
```
Java中提供一种更规范方法是使用ThreadLocal,这个类能使线程中的某个值与保存值的对象关联起来.
```
```
ThreadLocal提供get与set方法,为使用该变量的每个线程提供一份独立的副本.是一种典型的线程封闭概念.
```
#######Connection举例
```
为了不必要为每个方法传递一个Connection对象,所以将Connection对象作为全局对象处理.但是JDBC的连接对象不一定是线程安全的,
所以应该为每个线程保存一个Connection对象,这样符合使用ThreadLocal思想.
```
```java
private static ThreadLocal<Connection> connectionHolder 
	= new ThreadLocal<Connection>(){
    	public Connection initialValue(){
        	return DriverManager.getConnection(DB_URL);
        }
    }
public static Connection getConnection(){
	return connectionHolder.get();
}
```
Note:
```
1. 通过将JDBC的Connection保存到ThreadLocal对象中,这样每个线程都会拥有属于自己的连接.
```
```
2. 某个线程初次调用ThreadLocal.get方法时,会调用initialValue()这个方法.
```
#######如何理解ThreadLocal
```
可以将ThreadLocal< T >看做:Map<Thread, T> 对象,每次都会根据当前的Thread取到属于它的局部变量.
```
#######ThreadLocal几种常用方式
```
1. 可能某个操作需要一个临时变量,比如:缓冲区,同时又不希望每次执行都重新分配临时变量,就可以使用这种方式.将缓冲区与Thread绑定,这样即用即取.
```
```
2. 如果将一个单线程应用程序移植到多线程中,可以将所有的全局变量转换为ThreadLocal变量,可以维持线程安全性.
```
```
3. EJB中,J2EE容器需要将一个事务上下文与某个执行的线程关联,也应该使用ThreadLocal.
```
#######忠告
```
请不要滥用ThreadLocal,例如将所有的全局变量都作为ThreadLocal对象,或者作为一种"隐藏"方法参数的手段.
ThreadLocal会降低代码的可重用性,在类与类之间多加入了耦合性.
```

###3.4 不变性
```
不可变对象,一定是线程安全的.
```
```
如果一个对象是不可变对象,那么同步和并发问题都将不存在.
如果某个对象在被创建后其状态就不能被修改,那么这个对象就称为不可变对象.
```
##### 不可变对象条件
```
1. 对象创建后其状态就不能修改
```
```
2. 对象的所有域都是final类型.
```
```
3. 对象正确创建(在对象的创建期间,this引用没有逸出)
```
#####不可变对象举例
```java
@Immutable
public final class ThreeStooges {
    private final Set<String> stooges = new HashSet<String>();

    public ThreeStooges() {
        stooges.add("Moe");
        stooges.add("Larry");
        stooges.add("Curly");
    }

    public boolean isStooge(String name) {
        return stooges.contains(name);
    }

    public String getStoogeNames() {
        List<String> stooges = new Vector<String>();
        stooges.add("Moe");
        stooges.add("Larry");
        stooges.add("Curly");
        return stooges.toString();
    }
}
```
Note:
```
1. 尽管Set<String> stooges是可变的,但是创建后,外部无法对其进行修改
```
```
2. 对象的创建肯定正确,同时域也是fianl.
```
#####区别"不可变对象"与"不可变的对象引用"
```
其实,不可变对象可以通过将一个保存新状态的实例来"替换"原有的不可变对象.
```
##### 3.4.1 Final域
```
final类型的域是不能修改的,但是如果final类型修饰的对象是可变的,那么被引用的对象是可以修改的.
```
####### final关键字具有特殊的语义
```
final域能确保初始化过程的安全性,从而可以不受限制的访问不可变对象,并在共享这些对象时无须同步.
```


